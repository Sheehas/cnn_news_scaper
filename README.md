## ReadMe for CNN News Scraper

## Description
This Python program is designed to scrape recent news articles from the CNN website (https://edition.cnn.com/). It extracts news headlines and related links from various categories of the CNN website and allows you to save this data to either a CSV file or a SQLite database.

## Features
- Extracts news headlines and related links from CNN website.
- Organizes the retrieved data into categories.
- Saves the data to a CSV file with the current date as the filename.
- Saves the data to a SQLite database for later analysis.

## Requirements
Before running the program, make sure you have the following dependencies installed:
- Python 3.x
- aiohttp (for asynchronous HTTP requests)
- BeautifulSoup (for HTML parsing)
- sqlite3 (for SQLite databases)

You can install the necessary Python packages using the pip program:
```
pip install aiohttp beautifulsoup4
```

## How to use
1. Clone or download the program from the repository.
2. Open a terminal or command prompt and navigate to the directory containing the program file.
3. Run the program using the following command:
   ```
   python cnn_news_scraper.py
   ```

## Output
After running the program, you will get the following output:
- A CSV file named `<current_date>.csv` containing scanned news data.
- News data stored in a SQLite database named `news_database.db`.


## Important Notes
- The program is designed to scrape news data from the CNN website, and its functionality may depend on the structure of the site. Any changes to the site structure may require modification of the program.

Happy news scraping!
