import asyncio
import aiohttp
from bs4 import BeautifulSoup
import datetime
import sqlite3
import csv

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_category(session, category_url, queue):
    html = await fetch_url(session, category_url)
    soup = BeautifulSoup(html, 'lxml')

    name_elements = soup.find_all(class_='container__text container_lead-plus-headlines__text')
    link_elements = soup.find_all(class_='container__link container_lead-plus-headlines__link')

    for name_element, link_element in zip(name_elements, link_elements):
        name_news = name_element.text.strip()
        link_news = link_element.get('href').strip()

        await queue.put((name_news, link_news, category_url))

async def scrape_cnn_news():
    url = 'https://edition.cnn.com/'

    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        soup = BeautifulSoup(response, 'lxml')

        categorys = soup.find_all(class_='header__nav-item-link')

        queue = asyncio.Queue()

        tasks = []
        for category in categorys[:-1]:  # Remove None
            category_url = category.get('href')
            tasks.append(scrape_category(session, category_url, queue))

        await asyncio.gather(*tasks)
        news_list = []

        while not queue.empty():
            news_list.append(await queue.get())

    return news_list

def save_to_csv(news_list):
    datetime_file = datetime.datetime.now().date()
    filename = f'{datetime_file}.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(('name', 'link', 'category'))
        for name, link, category in news_list:
            writer.writerow((name, f'https://edition.cnn.com{link}', category.replace('https://edition.cnn.com/','')))

    return filename

def save_to_bd(news_list):
    conn = sqlite3.connect('news_database.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS news (
                        name TEXT,
                        link TEXT,
                        category TEXT,
                        date TEXT
                    )''')

    date = datetime.datetime.now().date()

    for name, link, category in news_list:
        cursor.execute("INSERT INTO news (name, link, category, date) VALUES (?, ?, ?, ?)",
                       (name, f'https://edition.cnn.com{link}', category.replace('https://edition.cnn.com/',''), date))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    news_list = loop.run_until_complete(scrape_cnn_news())
    loop.close()

    save_to_csv(news_list)
    save_to_bd(news_list)

    input(f'Count news - {len(news_list)}\n')

