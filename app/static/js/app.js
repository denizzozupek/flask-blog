// category

document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".nav-links .dropdown");
    if(dropdown) {
        const dropdownMenu = dropdown.querySelector(".dropdown-menu");
        // Hover (desktop)
        dropdown.addEventListener("mouseenter", () => dropdownMenu.style.display = "block");
        dropdown.addEventListener("mouseleave", () => dropdownMenu.style.display = "none");
        // Click (mobil)
        dropdown.addEventListener("click", (e) => {
            e.stopPropagation();
            dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
        });
        // Tıklama dışında kapanması
        document.addEventListener("click", (e) => {
            if(!dropdown.contains(e.target)) dropdownMenu.style.display = "none";
        });
    }
});

 // hamburger menu mobil 

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");
if(menuToggle && navLinks){
    menuToggle.addEventListener("click", () => navLinks.classList.toggle("active"));
    document.addEventListener("click", (e) => {
        if(!menuToggle.contains(e.target) && !navLinks.contains(e.target) && navLinks.classList.contains("active")){
            navLinks.classList.remove("active");
        }
    });
}


//searchbox

const searchToggle = document.getElementById("searchToggle");
const searchBox = document.querySelector(".search-box");
const closeBtn = document.getElementById("closeSearch");

searchToggle.addEventListener("click", (e) => {
    e.stopPropagation(); // sayfaya tıklama olayını engelle
    searchBox.style.display = searchBox.style.display === "block" ? "none" : "block";
    searchBox.querySelector("input").focus();
});

closeBtn.addEventListener("click", () => {
    searchBox.style.display = "none";
});

// boş alana tıklayınca kapanması
document.addEventListener("click", (e) => {
    if (!searchBox.contains(e.target) && e.target !== searchToggle) {
        searchBox.style.display = "none";
    }
});

