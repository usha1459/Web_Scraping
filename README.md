# IMDb Top 30 Movies Scraper

## Overview
This project scrapes the **IMDb Top 30 Movies** from the IMDb website and stores the extracted data in a CSV file. It uses **BeautifulSoup** for web scraping and **Pandas** for data processing.

## Features
✅ Scrapes the **Top 30 movies** from IMDb  
✅ Extracts **Title, Year, and IMDb Rating**  
✅ Saves the data to a **CSV file** for further analysis  
✅ Uses headers to mimic a real browser request  

## Technologies Used
- **Python**
- **Requests** (for fetching the webpage)
- **BeautifulSoup** (for web scraping)
- **Pandas** (for data manipulation)

## Installation & Setup

### Clone the repository:
```sh
git clone https://github.com/yourusername/imdb-movie-scraper.git
```

### Navigate to the project directory:
```sh
cd imdb-movie-scraper
```

### Install dependencies:
```sh
pip install requests beautifulsoup4 pandas
```

## Usage
Run the script using:
```sh
python imdb_scraper.py
```

The scraped data will be saved as **imdb_top_30_fixed.csv** in the project folder.

## Example Output
```plaintext
SI.No  Title                      Year  IMDb Rating
1      The Shawshank Redemption   1994  9.3
2      The Godfather             1972  9.2
...
```

## Contributing
Feel free to submit **issues** and **pull requests** to improve the script!

