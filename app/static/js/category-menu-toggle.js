document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    const dropdownLink = dropdown.querySelector("a");
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");

    // Masaüstü hover davranışı
    dropdown.addEventListener("mouseenter", function() {
        if (window.innerWidth > 768) {
            dropdownMenu.style.display = "block";
        }
    });

    dropdown.addEventListener("mouseleave", function() {
        if (window.innerWidth > 768) {
            dropdownMenu.style.display = "none";
        }
    });

    // Mobil toggle
    dropdownLink.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) {
            e.preventDefault(); // linke gitmeyi engelle
            dropdownMenu.style.display =
                dropdownMenu.style.display === "block" ? "none" : "block";
        }
    });
});
