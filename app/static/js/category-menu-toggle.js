document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    const dropdownLink = dropdown.querySelector("a");
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");
    
    let isToggling = false;
    let clickCount = 0; // Tıklama sayacı ekle

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

    // Tüm dropdown area'ya click event ekle (link + boşluk)
    dropdown.addEventListener("click", function(e) {
        if (window.innerWidth <= 768) {
            e.preventDefault();
            e.stopPropagation();
            
            // Çok hızlı tıklamaları ve çift tıklamaları önle
            if (isToggling) return;
            
            clickCount++;
            isToggling = true;
            
            console.log("Tıklama sayısı:", clickCount); // Debug için
            
            // Dropdown'un şu anki durumunu kontrol et
            const isOpen = dropdown.classList.contains("active");
            
            if (isOpen) {
                dropdown.classList.remove("active");
                dropdownMenu.style.display = "none";
            } else {
                dropdown.classList.add("active");
                dropdownMenu.style.display = "block";
            }
            
            // Toggle flag'ini daha uzun süre tut
            setTimeout(() => {
                isToggling = false;
            }, 200);
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