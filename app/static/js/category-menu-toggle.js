document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    const dropdownLink = dropdown.querySelector("a");
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");
    
    let isToggling = false; // Toggle işlemini kontrol etmek için flag

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

    // Mobil toggle - daha güvenli yöntem
    dropdownLink.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) {
            e.preventDefault();
            e.stopPropagation(); // Event bubbling'i durdur
            
            // Çok hızlı tıklamaları önle
            if (isToggling) return;
            
            isToggling = true;
            
            // Dropdown'un şu anki durumunu kontrol et
            const isOpen = dropdownMenu.style.display === "block" || 
                          dropdown.classList.contains("active");
            
            if (isOpen) {
                dropdownMenu.style.display = "none";
                dropdown.classList.remove("active");
            } else {
                dropdownMenu.style.display = "block";
                dropdown.classList.add("active");
            }
            
            // Kısa bir süre sonra toggle flag'ini sıfırla
            setTimeout(() => {
                isToggling = false;
            }, 100);
        }
    });

    // Dışarıya tıklandığında dropdown'u kapat (mobil için)
    document.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) {
            if (!dropdown.contains(e.target)) {
                dropdownMenu.style.display = "none";
                dropdown.classList.remove("active");
            }
        }
    });

    // Window resize olduğunda dropdown'u sıfırla
    window.addEventListener("resize", function() {
        if (window.innerWidth > 768) {
            dropdownMenu.style.display = "";
            dropdown.classList.remove("active");
        }
    });
});