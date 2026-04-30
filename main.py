import random
import statistics
import matplotlib.pyplot as plt

import movie_storage_sql as storage
import movie_api as api
import website_generator as webgen

title = "My Movies Database"
width = 42

print("*" * width)
print(title.center(width))
print("*" * width)
# =========================
# MENU
# =========================

def print_menu():
    """Display the main menu options to the user."""
    print("\nMenu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie (via API)")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("9. Generate website")
    print("10. Rating histogram")
    print("11. Sort by year")
    print("12. Filter movies")
    print("13. Rating bar chart")


def pause():
    input("\nPress enter to continue ")


# =========================
# COMMAND FUNCTIONS
# =========================

def command_list_movies():
    movies = storage.list_movies()

    print(f"\n{len(movies)} movies in total")

    for title, data in movies.items():
        print(f"{title} ({data['year']}): {data['rating']}")


def command_add_movie():
    title = input("Enter movie name: ").strip()

    if not title:
        print("Invalid title.")
        return

    movies = storage.list_movies()
    if title in movies:
        print("Movie already exists!")
        return

    print("Fetching data from API...")

    data = api.fetch_movie(title)

    if not data:
        print("❌ Movie not found.")
        return

    try:
        movie_title = data["title"]
        year = int(data["year"])
        rating = float(data["rating"])
    except (KeyError, ValueError):
        print("⚠️ Invalid data from API.")
        return

    print("\nMovie found:")
    print(f"Title: {movie_title}")
    print(f"Year: {year}")
    print(f"Rating: {rating}")

    poster_url = input("Enter poster URL (press Enter to use API/default): ").strip()
    if not poster_url:
        poster_url = data.get("poster", "")

    trailer_url = input("Enter trailer URL (press Enter to use API/default): ").strip()
    if not trailer_url:
        trailer_url = data.get("trailer", "")

    print("\nFinal Preview:")
    print(f"Title: {movie_title}")
    print(f"Year: {year}")
    print(f"Rating: {rating}")
    print(f"Poster: {poster_url}")
    print(f"Trailer: {trailer_url}")

    storage.add_movie(
        movie_title,
        year,
        rating,
        poster_url,
        trailer_url
    )

    print("\n✅ Movie added successfully!")


def command_delete_movie():
    title = input("Enter movie to delete: ")
    storage.delete_movie(title)


def command_update_movie():
    title = input("Movie name: ")

    try:
        rating = float(input("New rating: "))
    except ValueError:
        print("Invalid rating.")
        return

    storage.update_movie(title, rating)


def command_statistics():
    movies = storage.list_movies()

    if not movies:
        print("No movies available.")
        return

    ratings = [m["rating"] for m in movies.values()]

    print("Average:", round(statistics.mean(ratings), 2))
    print("Median:", round(statistics.median(ratings), 2))


def command_random_movie():
    movies = storage.list_movies()

    if not movies:
        print("No movies available.")
        return

    title = random.choice(list(movies.keys()))
    print(title, movies[title])


def command_search_movie():
    movies = storage.list_movies()
    text = input("Search: ").lower()

    found = False

    for title, data in movies.items():
        if text in title.lower():
            print(f"{title} ({data['year']}): {data['rating']}")
            found = True

    if not found:
        print("No matches found.")


def command_sort_by_rating():
    movies = storage.list_movies()

    sorted_movies = sorted(
        movies.items(),
        key=lambda x: x[1]["rating"],
        reverse=True
    )

    for title, data in sorted_movies:
        print(f"{title} ({data['year']}): {data['rating']}")


def command_generate_website():
    movies = storage.list_movies()
    webgen.generate(movies)
    print("🌐 Website generated successfully.")


def command_histogram():
    movies = storage.list_movies()
    ratings = [m["rating"] for m in movies.values()]

    plt.hist(ratings, bins=10)
    plt.title("Ratings Histogram")
    plt.show()


def command_sort_by_year():
    movies = storage.list_movies()

    sorted_movies = sorted(
        movies.items(),
        key=lambda x: x[1]["year"],
        reverse=True
    )

    for title, data in sorted_movies:
        print(f"{title} ({data['year']}): {data['rating']}")


def command_filter_movies():
    movies = storage.list_movies()

    try:
        min_rating = float(input("Min rating: "))
    except ValueError:
        print("Invalid input.")
        return

    for title, data in movies.items():
        if data["rating"] >= min_rating:
            print(f"{title} ({data['year']}): {data['rating']}")


def command_bar_chart():
    movies = storage.list_movies()

    titles = list(movies.keys())
    ratings = [m["rating"] for m in movies.values()]

    plt.bar(titles, ratings)
    plt.xticks(rotation=45)
    plt.title("Movie Ratings")
    plt.show()


# =========================
# MAIN LOOP
# =========================

def main():
    storage.create_table()

    while True:
        print_menu()
        choice = input("Choice (0-13): ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            command_list_movies()
        elif choice == "2":
            command_add_movie()
        elif choice == "3":
            command_delete_movie()
        elif choice == "4":
            command_update_movie()
        elif choice == "5":
            command_statistics()
        elif choice == "6":
            command_random_movie()
        elif choice == "7":
            command_search_movie()
        elif choice == "8":
            command_sort_by_rating()
        elif choice == "9":
            command_generate_website()
        elif choice == "10":
            command_histogram()
        elif choice == "11":
            command_sort_by_year()
        elif choice == "12":
            command_filter_movies()
        elif choice == "13":
            command_bar_chart()
        else:
            print("Invalid choice.")

        pause()


if __name__ == "__main__":
    main()