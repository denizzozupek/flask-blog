document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    const trigger = dropdown.querySelector("a");
    const menu = dropdown.querySelector(".dropdown-menu");

    function toggleMenu(e) {
        e.preventDefault();
        e.stopPropagation();
        dropdown.classList.toggle("active");
    }

    // Mobil için: pointerdown olursa anında yakala
    trigger.addEventListener("pointerdown", function(e) {
        if (window.innerWidth <= 768) toggleMenu(e);
    }, { passive: false });

    // Fallback: click (masaüstünde de çalışır)
    trigger.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) toggleMenu(e);
    });

    // Dışarı tıklayınca kapat
    document.addEventListener("click", function(e) {
        if (window.innerWidth <= 768 && !dropdown.contains(e.target)) {
            dropdown.classList.remove("active");
        }
    });

    // Resize olunca sıfırla
    window.addEventListener("resize", function() {
        if (window.innerWidth > 768) {
            dropdown.classList.remove("active");
        }
    });
});
