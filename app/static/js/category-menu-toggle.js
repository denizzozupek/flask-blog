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
            e.preventDefault(); // ÖNEMLİ: sayfayı yönlendirme
            // toggle dropdown
            if (dropdownMenu.style.display === "block") {
                dropdownMenu.style.display = "none";
            } else {
                dropdownMenu.style.display = "block";
            }
        }
    });
});
