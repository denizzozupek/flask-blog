document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");

    // Masaüstü için hover davranışı
    dropdown.addEventListener("mouseenter", function() {
        if (window.innerWidth > 768) { // mobil değilse
            dropdownMenu.style.display = "block";
        }
    });

    dropdown.addEventListener("mouseleave", function() {
        if (window.innerWidth > 768) {
            dropdownMenu.style.display = "none";
        }
    });

    // Mobil için toggle (click)
    dropdown.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) { // sadece mobilde çalışsın
            e.preventDefault(); // linke gitmeyi engelle
            dropdownMenu.style.display =
                dropdownMenu.style.display === "block" ? "none" : "block";
        }
    });
});
