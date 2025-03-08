import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb Top 250 movies URL
URL = "https://www.imdb.com/chart/top/"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Fetch webpage
response = requests.get(URL, headers=HEADERS)

# Check if request was successful
if response.status_code != 200:
    print("Failed to fetch IMDb data. Check if the website has blocked requests.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Find movie list container
movies = soup.select("li.ipc-metadata-list-summary-item")[:30]  # Get top 30 movies

# Extract data
movie_data = []
for idx, movie in enumerate(movies, start=1):  # Adding SI.No
    # Extract title
    title_tag = movie.select_one("h3")
    title = title_tag.text.strip().split(". ", 1)[-1] if title_tag else "N/A"

    # Extract year
    year_tag = movie.find("span", class_="sc-d5ea4b9d-7")
    year = year_tag.text.strip() if year_tag else "N/A"

    # Extract IMDb rating
    rating_tag = movie.select_one("span.ipc-rating-star--imdb")
    rating = rating_tag.text.strip().split(" ")[0] if rating_tag else "N/A"  # Extract only rating number

    movie_data.append([idx, title, year, rating])

# Convert to DataFrame
df = pd.DataFrame(movie_data, columns=["SI.No", "Title", "Year", "IMDb Rating"])

# Display output
print(df)

# Save as CSV
df.to_csv("imdb_top_30_fixed.csv", index=False)
print("\nData saved as 'imdb_top_30_fixed.csv'")
