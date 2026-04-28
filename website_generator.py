def generate(movies):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My Movie APP</title>

<style>

/* RESET */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* BODY */
body {
    font-family: Monaco;
    background: #F5F5F0;
}

/* NAVBAR */
.navbar {
    padding: 50px;
    background:#009B50;
    text-align: center;
    
}

.navbar h1 {
    color: white;
}

/* GRID */
.container {
    display: flex;
    flex-direction: row;
    grid-template-columns: repeat(auto-fill, 1fr);
    gap: 30px;
    justify-content: center;
    padding:10px 15px;
    margin-top: 20px
    
}

/* MOVIE CARD */
.movie {
    cursor: pointer;
    text-align: center;
    transition: 0.3s;
}

.movie:hover {
    transform: scale(1.05);
}

/* POSTER */
.movie img {
    width: 140px;
    height: 193px;
    object-fit: cover;
    display: block;
    box-shadow: 0 3px 6px rgba(0,0,0,0.2);
}

/* TEXT */
.movie h2 {
    font-size: 0.85em;
    margin-top: 8px;
}

.movie p {
    font-size: 0.75em;
    color: #666;
}

/* MODAL BACKGROUND */
.modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;

    background-color: rgba(0,0,0,0.7);
}

/* MODAL CONTENT */
.modal-content {
    background: white;
    margin: 5% auto;
    padding: 20px;
    width: 60%;
    max-width: 700px;
    text-align: center;
}

/* CLOSE BUTTON */
.close {
    float: right;
    font-size: 28px;
    cursor: pointer;
}

/* BUTTON */
button {
    margin-top: 10px;
    padding: 8px 16px;
    background: #009B50;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #007a3d;
}

</style>
</head>

<body>

<nav class="navbar">
  <h1>My Movie APP</h1>
</nav>

<div class="container">
"""

    for i, (title, data) in enumerate(movies.items()):
        poster = data.get("poster_url", "")
        trailer = data.get("trailer_url", "")

        html += f"""
        <div class="movie" onclick="openModal({i})">
            <img src="{poster}" alt="{title}">
            <h2>{title}</h2>
            <p>{data['year']}</p>
            <p>⭐ {data['rating']}</p>
        </div>

        <div id="modal{i}" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal({i})">&times;</span>
                <h2>{title}</h2>
                <p>Year: {data['year']}</p>
                <p>Rating: ⭐ {data['rating']}</p>

                <iframe width="100%" height="400"
                    src="{trailer}"
                    frameborder="0"
                    allowfullscreen>
                </iframe>

                <br>
                <a href="{trailer}" target="_blank">
                    <button>▶ Play Trailer</button>
                </a>
            </div>
        </div>
        """

    html += """
</div>

<script>
function openModal(id) {
    document.getElementById("modal" + id).style.display = "block";
}

function closeModal(id) {
    document.getElementById("modal" + id).style.display = "none";
}

window.onclick = function(event) {
    let modals = document.getElementsByClassName("modal");
    for (let i = 0; i < modals.length; i++) {
        if (event.target === modals[i]) {
            modals[i].style.display = "none";
        }
    }
}
</script>

</body>
</html>
"""

    with open("movies.html", "w", encoding="utf-8") as f:
        f.write(html)