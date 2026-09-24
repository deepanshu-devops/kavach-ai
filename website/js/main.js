/* ==========================================================================
   Kavach-AI — site interactions
   ========================================================================== */

(function () {
  "use strict";

  // ---------- Navigation: fixed shadow + mobile menu ----------
  const nav = document.getElementById("nav");
  const navInner = document.getElementById("navInner");
  const burger = document.getElementById("burger");

  const onScroll = () => {
    if (nav) nav.classList.toggle("scrolled", window.scrollY > 24);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (burger && navInner) {
    burger.addEventListener("click", () => {
      const open = navInner.classList.toggle("menu-open");
      burger.classList.toggle("open", open);
      burger.setAttribute("aria-expanded", String(open));
    });
    // Close mobile menu on navigation
    navInner.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        navInner.classList.remove("menu-open");
        burger.classList.remove("open");
      })
    );
  }

  // ---------- Reveal on scroll ----------
  const revealed = document.querySelectorAll("[data-reveal]");

  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealed.forEach((el) => io.observe(el));
  } else {
    revealed.forEach((el) => el.classList.add("revealed"));
  }

  // ---------- Demo form ----------
  const form = document.getElementById("demoForm");
  const toast = document.getElementById("toast");
  const toastMsg = document.getElementById("toastMsg");

  const showToast = (msg) => {
    if (!toast) return;
    if (toastMsg) toastMsg.textContent = msg;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 4200);
  };

  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = form.querySelector("#name");
      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
        showToast("Please enter a valid work email.");
        email.focus();
        return;
      }
      showToast("Request sent — we'll be in touch shortly.");
      form.reset();
    });
  }
})();