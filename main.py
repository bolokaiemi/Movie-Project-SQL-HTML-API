import random
import statistics

import movie_storage_sql as storage
import movie_api as api
import website_generator as webgen


user_id = 1
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



def pause():
    """Pause execution until the user presses Enter."""
    input("\nPress enter to continue ")


# =========================
# COMMAND FUNCTIONS
# =========================

def command_list_movies():
    """Retrieve all movies from storage and display them."""
    movies = storage.list_movies(user_id)

    print(f"\n{len(movies)} movies in total")

    for movie_title, data in movies.items():
        print(f"{movie_title} ({data['year']}): {data['rating']}")


def command_add_movie():
    """
    Add a new movie using data fetched from an external API.

    Prompts the user for a movie title, fetches its data,
    validates the response, and stores it in the database.
    """
    movie_title = input("Enter movie name: ").strip()

    if not movie_title:
        print("Invalid title.")
        return

    movies = storage.list_movies(user_id)
    if movie_title in movies:
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

    # Optional preview
    print("\nPreview:")
    print(f"Title: {movie_title}")
    print(f"Year: {year}")
    print(f"Rating: {rating}")

    storage.add_movie(movie_title, year, rating)

    print("\n✅ Movie added successfully!")


def command_delete_movie():
    """Delete a movie from storage based on user input."""
    movie_title = input("Enter movie to delete: ")
    storage.delete_movie(movie_title)


def command_update_movie():
    """
    Update the rating of an existing movie.

    Prompts the user for a movie title and a new rating value.
    """
    movie_title = input("Movie name: ")

    try:
        rating = float(input("New rating: "))
    except ValueError:
        print("Invalid rating.")
        return

    storage.update_movie(movie_title, rating)


def command_statistics():
    """
    Display statistical information about movie ratings.

    Calculates and prints the average and median ratings.
    """
    movies = storage.list_movies()

    if not movies:
        print("No movies available.")
        return

    ratings = [m["rating"] for m in movies.values()]

    print("Average:", round(statistics.mean(ratings), 2))
    print("Median:", round(statistics.median(ratings), 2))


def command_random_movie():
    """Select and display a random movie from storage."""
    movies = storage.list_movies()

    if not movies:
        print("No movies available.")
        return

    movie_title = random.choice(list(movies.keys()))
    print(movie_title, movies[title])


def command_search_movie():
    """
    Search for movies by title substring.

    Performs a case-insensitive search and displays matches.
    """
    movies = storage.list_movies()
    text = input("Search: ").lower()

    found = False

    for movie_title, data in movies.items():
        if text in movie_title.lower():
            print(f"{movie_title} ({data['year']}): {data['rating']}")
            found = True

    if not found:
        print("No matches found.")


def command_sort_by_rating():
    """Display all movies sorted by rating in descending order."""
    movies = storage.list_movies()

    sorted_movies = sorted(
        movies.items(),
        key=lambda x: x[1]["rating"],
        reverse=True
    )

    for movie_title, data in sorted_movies:
        print(f"{movie_title} ({data['year']}): {data['rating']}")


def command_generate_website():
    """
    Generate a static website displaying all movies.

    Uses the website_generator module.
    """
    movies = storage.list_movies(user_id)
    webgen.generate(movies)
    print("🌐 Website generated successfully.")




# =========================
# MAIN LOOP
# =========================

def main():
    """
    Run the main application loop.

    Initializes storage and repeatedly prompts the user
    to select an action from the menu.
    """
    storage.create_table()

    while True:
        print_menu()
        choice = input("Choice: ")

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
        else:
            print("Invalid choice.")

        pause()


if __name__ == "__main__":
    main()