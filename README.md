# Movie Database App

A multi-user movie collection application built with Python, SQLite, and a dynamic website generator.

## Overview

This project allows users to create and manage their own personal movie collections. Each user has a separate profile, ensuring that movie lists are private and customized.

The application fetches movie data from an external API and generates a visually appealing website displaying the collection.

### Features
👤 User Profiles
Create and switch between multiple users
Each user has their own movie collection
🎬 Movie Management
Add movies via API
Delete movies
Update movies with personal notes
📊 Movie Data
Title, year, rating
Poster image
Country (with flag)
Trailer link
🌐 Website Generator
Generates a personal HTML page per user
Responsive grid layout
Hover effects and clean UI
Click poster → opens IMDb
Click “Watch Trailer” → opens trailer
⚡ JavaScript Enhancements
Smooth hover animations
Ready for future features (search/filter)

#### Tech Stack
🐍 Python (core logic)
🗄 SQLite (database)
🌐 OMDb API (movie data)
🧱 HTML & CSS (frontend)
⚡ JavaScript (UI enhancements)

##### Project Structure

project/
│
├── movies.py                # Main application (CLI)
├── movie_storage_sql.py     # Database handling
├── movie_api.py             # API integration
├── website_generator.py     # HTML generator
├── movies.db                # SQLite database
└── README.md

⚙️ How It Works
User selects or creates a profile
Movie data is fetched from the API
Data is stored in SQLite database
Website is generated using stored data
User views their collection in the browser

###### Usage

Run the application:

python movies.py
Menu Options:
List movies
Add movie
Delete movie
Update movie (add note)
Generate website
Switch user

🌐 Website Output

Each user gets their own HTML file:

John.html
Sara.html

Features:

Poster display
Ratings overlay
Country flags
Notes on hover
Trailer links
🧪 Example Flow
Create user: Sara
Add movie: Titanic
Add note: "My favorite movie!"
Generate website
Open Sara.html
💡 Future Improvements
🔍 Search functionality in website
🎥 Embedded YouTube trailers
❤️ Favorites system
📱 Mobile optimization
☁️ Deployment (web app)

####### Requirements
Python 3.x
matplotlib (optional for charts)

Install dependencies:

pip install matplotlib

📄 License

This project is for educational purposes.
