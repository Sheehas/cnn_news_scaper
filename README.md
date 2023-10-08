# ReadMe for CNN News Scraper


## Description
This Python program is designed to scrape the latest news articles from CNN's website (https://edition.cnn.com/). It retrieves news headlines and their associated links from various categories on the CNN website and allows you to save this data to both a CSV file and a SQLite database.


## Features
- Scrapes news headlines and links from CNN's website.
- Organizes the scraped data by category.
- Saves the data to a CSV file with the current date as the filename.
- Stores the data in a SQLite database for further analysis.


## Requirements
Before running the program, ensure you have the following dependencies installed:
- Python 3.x
- aiohttp (for asynchronous HTTP requests)
- BeautifulSoup (for HTML parsing)
- sqlite3 (for SQLite database operations)


You can install the required Python packages using pip:
```
pip install aiohttp beautifulsoup4
```


## How to Use
1. Clone or download the program from the repository.
2. Open a terminal or command prompt and navigate to the directory containing the program file.
3. Run the program using the following command:
   ```
   python cnn_news_scraper.py
   ```


## Output
After running the program, you will get the following output:
- A CSV file named `<current_date>.csv` containing the scraped news data.
- News data stored in a SQLite database named `news_database.db`.


## Important Notes
- The program is designed to scrape news data from the CNN website, and its functionality may depend on the website's structure. Any changes to the website's structure may require modifications to the program.
- Please be aware of website scraping policies and terms of service for CNN. Make sure your use of this program complies with the website's terms and conditions.


## Contact
If you have any questions, suggestions, or encounter issues with this program, you can contact the author at [your_email@example.com].


Happy news scraping!
