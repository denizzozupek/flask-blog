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
