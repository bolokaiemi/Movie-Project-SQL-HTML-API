def country_to_flag(country):
    mapping = {
        "USA": "us",
        "United States": "us",
        "UK": "gb",
        "Germany": "de",
        "France": "fr",
        "India": "in",
        "Spain": "es",
        "Italy": "it",
        "Japan": "jp",
        "Canada": "ca"
    }

    code = mapping.get(country, None)
    return f"https://flagcdn.com/w40/{code}.png" if code else ""


def generate(movies, username="User"):

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{username}'s Movies</title>

<style>
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: Arial, sans-serif;
    background: #111;
    color: white;
}}

.navbar {{
    padding: 20px;
    background:#009B50;
    text-align: center;
}}

.container {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 20px;
    padding: 20px;
}}

.movie {{
    background: #1c1c1c;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    cursor: pointer;
    transition: 0.3s;
}}

.movie:hover {{
    transform: scale(1.05);
}}

.movie img {{
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-radius: 8px;
}}

.flag {{
    width: 30px;
    margin-top: 5px;
}}

.note {{
    font-size: 12px;
    color: #bbb;
}}

.modal {{
    display: none;
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.8);
}}

.modal-content {{
    background: #222;
    margin: 5% auto;
    padding: 20px;
    width: 80%;
    max-width: 700px;
}}

.close {{
    float: right;
    font-size: 28px;
    cursor: pointer;
}}

button {{
    margin-top: 10px;
    padding: 8px 16px;
    background: #e50914;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}}
</style>
</head>

<body>

<nav class="navbar">
<h1>{username}'s Movie Collection 🎬</h1>
</nav>

<div class="container">
"""

    for i, (title, movie) in enumerate(movies.items()):

        poster = movie.get("poster") or movie.get("poster_url") or "https://via.placeholder.com/300x450"
        trailer = movie.get("trailer") or movie.get("trailer_url") or ""

        if "watch?v=" in trailer:
            trailer = trailer.replace("watch?v=", "embed/")

        flag = country_to_flag(movie.get("country"))

        html += f"""
<div class="movie" onclick="openModal({i})">
<img src="{poster}">
<h3>{title}</h3>
<p>⭐ {movie.get('rating')}</p>
<p>{movie.get('year')}</p>
{"<img class='flag' src='" + flag + "'>" if flag else ""}
<div class="note">{movie.get('note','')}</div>
</div>

<div id="modal{i}" class="modal">
<div class="modal-content">
<span class="close" onclick="closeModal({i})">&times;</span>

<h2>{title}</h2>
<p>{movie.get('year')}</p>
<p>⭐ {movie.get('rating')}</p>

<iframe width="100%" height="400" src="{trailer}" frameborder="0" allowfullscreen></iframe>
</div>
</div>
"""

    html += """
</div>

<script>
function openModal(id){document.getElementById("modal"+id).style.display="block";}
function closeModal(id){document.getElementById("modal"+id).style.display="none";}
</script>

</body>
</html>
"""

    with open(f"{username}.html", "w", encoding="utf-8") as f:
        f.write(html)