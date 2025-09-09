document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    menuToggle.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });

    document.addEventListener("click", (e) => {
        if (!menuToggle.contains(e.target) && !navLinks.contains(e.target) && navLinks.classList.contains("active")) {
            navLinks.classList.remove("active");
        }
    });
});