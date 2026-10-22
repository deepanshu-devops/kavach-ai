#!/usr/bin/env python3
"""
Kavach-AI — brand asset generator.

Regenerates `docs/assets/logo.png` from the same geometry that `docs/assets/logo.svg`
describes, so the PNG favicon stays in sync with the SVG mark.

Usage:
    python tools/generate_logo.py

Requires: Pillow + NumPy (`python -m pip install pillow numpy`).

The logo is the light-theme Kavach mark:
  * rounded light tile (white -> #e6eefc) with a soft brand edge,
  * gradient armour shield (#2f9fe0 -> #7c3aed -> #c026d3),
  * green verified check (#5fc98a -> #3f8f2a).
"""

from __future__ import annotations

import os

import numpy as np
from PIL import Image, ImageDraw

# --------------------------------------------------------------------------
# Geometry (viewBox units, 48x48) — keep in sync with docs/assets/logo.svg
# --------------------------------------------------------------------------

VIEWBOX = 48.0
SIZE = 512
SS = 4  # supersampling factor for smooth edges
DEVICE = SIZE * SS

TILE = (1.4, 1.4, 46.6, 46.6)  # x0, y0, x1, y1
TILE_RADIUS = 13.0
TILE_STROKE = 1.8

SHIELD_STROKE = 2.6
SPINE_STROKE = 0.9
SPINE_OPACITY = 0.28
CHECK_STROKE = 2.8

# Palette (light theme)
K_BG = [(0.0, (255, 255, 255)), (0.55, (242, 247, 254)), (1.0, (230, 238, 252))]
K_EDGE = [(0.0, (142, 198, 247)), (0.5, (179, 163, 242)), (1.0, (242, 174, 232))]
K_SHIELD = [(0.0, (47, 159, 224)), (0.55, (124, 58, 237)), (1.0, (192, 38, 211))]
K_CHECK = [(0.0, (95, 201, 138)), (1.0, (63, 143, 42))]
K_SPINE = (47, 159, 224)


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def scale(value: float) -> float:
    """viewBox units -> device pixels (supersampled)."""
    return value * (SIZE / VIEWBOX) * SS


def cubic(p0, p1, p2, p3, steps: int = 64):
    """Flatten a cubic bezier into a list of points."""
    pts = []
    for i in range(1, steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def shield_points():
    """Flatten the SVG shield path: M24 10.5 L34.5 14.6 V25 C... C... V14.6 Z"""
    pts = [(24.0, 10.5), (34.5, 14.6), (34.5, 25.0)]
    pts += cubic((34.5, 25.0), (34.5, 32.1), (30.1, 37.0), (24.0, 39.5))
    pts += cubic((24.0, 39.5), (17.9, 37.0), (13.5, 32.1), (13.5, 25.0))
    pts += [(13.5, 14.6), (24.0, 10.5)]
    return pts


def check_points():
    """M18.5 24.9 l3.7 3.7 l7.6 -8.4"""
    return [(18.5, 24.9), (22.2, 28.6), (29.8, 20.2)]


def diagonal_gradient(stops, bbox) -> Image.Image:
    """RGBA gradient image, painted top-left -> bottom-right across `bbox`."""
    x0, y0, x1, y1 = bbox
    span = max((x1 - x0) + (y1 - y0), 1e-6)
    ys, xs = np.mgrid[0:DEVICE, 0:DEVICE]
    t = np.clip(((xs - x0) + (ys - y0)) / span, 0.0, 1.0)

    offsets = np.array([s[0] for s in stops], dtype=np.float64)
    colors = np.array([s[1] for s in stops], dtype=np.float64)
    rgb = np.empty((DEVICE, DEVICE, 3), dtype=np.uint8)
    for channel in range(3):
        rgb[:, :, channel] = np.interp(t, offsets, colors[:, channel]).astype(np.uint8)

    alpha = np.full((DEVICE, DEVICE, 1), 255, dtype=np.uint8)
    return Image.fromarray(np.concatenate([rgb, alpha], axis=2), "RGBA")


def new_mask() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    mask = Image.new("L", (DEVICE, DEVICE), 0)
    return mask, ImageDraw.Draw(mask)


def stamp(base: Image.Image, mask: Image.Image, color_img: Image.Image) -> Image.Image:
    """Composite `color_img` onto `base` through `mask` (proper alpha blending)."""
    layer = color_img.copy()
    layer.putalpha(mask)
    return Image.alpha_composite(base, layer)


def stroke_mask(points, width, closed: bool = False) -> Image.Image:
    """Mask of a polyline stroke with round caps and round joins."""
    mask, draw = new_mask()
    pts = [(scale(x), scale(y)) for x, y in points]
    w = max(int(round(width * (SIZE / VIEWBOX) * SS)), 1)
    if closed:
        pts = pts + [pts[0]]
    draw.line(pts, fill=255, width=w, joint="curve")
    r = w / 2
    for x, y in pts:
        draw.ellipse([x - r, y - r, x + r, y + r], fill=255)
    return mask


def bbox_of(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (min(xs), min(ys), max(xs), max(ys))


def dev_bbox(points):
    x0, y0, x1, y1 = bbox_of(points)
    return (scale(x0), scale(y0), scale(x1), scale(y1))


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def build_logo() -> Image.Image:
    canvas = Image.new("RGBA", (DEVICE, DEVICE), (0, 0, 0, 0))

    # --- tile fill -------------------------------------------------------
    tile_box = (scale(TILE[0]), scale(TILE[1]), scale(TILE[2]), scale(TILE[3]))
    fill_mask, draw = new_mask()
    draw.rounded_rectangle(list(tile_box), radius=scale(TILE_RADIUS), fill=255)
    canvas = stamp(canvas, fill_mask, diagonal_gradient(K_BG, tile_box))

    # --- tile edge -------------------------------------------------------
    # SVG strokes are centred on the path, so the ring straddles the tile edge.
    stroke_px = scale(TILE_STROKE)
    outer = (
        tile_box[0] - stroke_px / 2,
        tile_box[1] - stroke_px / 2,
        tile_box[2] + stroke_px / 2,
        tile_box[3] + stroke_px / 2,
    )
    inner = (
        tile_box[0] + stroke_px / 2,
        tile_box[1] + stroke_px / 2,
        tile_box[2] - stroke_px / 2,
        tile_box[3] - stroke_px / 2,
    )
    edge_mask, draw = new_mask()
    draw.rounded_rectangle(list(outer), radius=scale(TILE_RADIUS) + stroke_px / 2, fill=255)
    draw.rounded_rectangle(list(inner), radius=scale(TILE_RADIUS) - stroke_px / 2, fill=0)
    canvas = stamp(canvas, edge_mask, diagonal_gradient(K_EDGE, tile_box))

    # --- shield ----------------------------------------------------------
    shield = shield_points()
    shield_mask = stroke_mask(shield, SHIELD_STROKE, closed=True)
    canvas = stamp(canvas, shield_mask, diagonal_gradient(K_SHIELD, dev_bbox(shield)))

    # --- shield spine ----------------------------------------------------
    spine_mask = stroke_mask([(24.0, 15.4), (24.0, 34.3)], SPINE_STROKE)
    spine_mask = spine_mask.point(lambda v: int(v * SPINE_OPACITY))
    spine_layer = Image.new("RGBA", (DEVICE, DEVICE), K_SPINE + (255,))
    canvas = stamp(canvas, spine_mask, spine_layer)

    # --- verified check --------------------------------------------------
    check = check_points()
    check_mask = stroke_mask(check, CHECK_STROKE)
    canvas = stamp(canvas, check_mask, diagonal_gradient(K_CHECK, dev_bbox(check)))

    return canvas.resize((SIZE, SIZE), Image.LANCZOS)


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "docs", "assets", "logo.png")
    logo = build_logo()
    logo.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({logo.size[0]}x{logo.size[1]}, {logo.mode})")


if __name__ == "__main__":
    main()
