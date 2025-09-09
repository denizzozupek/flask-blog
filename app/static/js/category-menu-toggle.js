document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");

    // Mouse dropdown üzerine gelince aç
    dropdown.addEventListener("mouseenter", function() {
        dropdownMenu.style.display = "block";
    });

    // Mouse dropdown’tan çıkınca kapat
    dropdown.addEventListener("mouseleave", function() {
        dropdownMenu.style.display = "none";
    });
});

