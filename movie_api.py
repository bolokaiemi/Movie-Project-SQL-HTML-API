import requests

API_KEY = "f5055ab1"

def fetch_movie(title):
    """Fetch movie data from OMDb API."""

    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data, "getting data")

        # ❌ Movie not found
        if data.get("Response") == "False":
            return None

        # ✅ Clean + consistent return format
        return {
            "title": data.get("Title"),
            "year": int(data.get("Year")) if data.get("Year") else 0,
            "rating": float(data.get("imdbRating")) if data.get("imdbRating") not in (None, "N/A") else 0.0,
            "plot": data.get("Plot", "N/A")
        }

    except Exception as e:
        print("API error:", e)
        return None