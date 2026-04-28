let moviesData = {};

// =========================
// LOAD MOVIES (NO API)
// =========================
function loadMovies() {
    const container = document.getElementById("movies");
    container.innerHTML = "";

    for (let title in moviesData) {
        let m = moviesData[title];

        container.innerHTML += `
            <div class="movie">
                <h3>${title}</h3>
                <p>${m.year}</p>
                <p>${m.rating}</p>
            </div>
        `;
    }
}

// =========================
// SEARCH MOVIES
// =========================
function searchMovie() {
    let val = document.getElementById("search").value.toLowerCase();
    let movies = document.getElementsByClassName("movie");

    for (let m of movies) {
        m.style.display = m.innerText.toLowerCase().includes(val)
            ? "block"
            : "none";
    }
}

// =========================
// SAMPLE DATA (NO BACKEND)
// =========================
moviesData = {
    "Inception": { year: 2010, rating: 8.8 },
    "Interstellar": { year: 2014, rating: 8.6 },
    "The Matrix": { year: 1999, rating: 8.7 }
};
function toggleMenu() {
    document.getElementById("menuDropdown").classList.toggle("show");
}

function toggleCategories() {
    document.getElementById("categoryDropdown").classList.toggle("show");
}

function openModal(id) {
    document.getElementById("modal" + id).style.display = "block";
}

function closeModal(id) {
    document.getElementById("modal" + id).style.display = "none";
}

// Close when clicking outside modal
window.onclick = function(event) {
    let modals = document.getElementsByClassName("modal");
    for (let i = 0; i < modals.length; i++) {
        if (event.target === modals[i]) {
            modals[i].style.display = "none";
        }
    }
}

// Auto load
loadMovies();