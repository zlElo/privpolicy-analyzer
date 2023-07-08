import requests
from bs4 import BeautifulSoup
import json
from analyse.sentiment import *
from analyse.language_detection import *
from loading_modules.loader import *

# if the standard webscraping function fail, this alternate scraping function will try also to scrape the datas from the website
def alternate_scrape(url):
    response = requests.get(url)
    title_count = 0
    subtitles_data = {}

    if response.status_code == 200:
        print('[log] Webscraping running...')
        soup = BeautifulSoup(response.text, "html.parser")
        subtitles = soup.find_all("h3")
        print('[log] found all subtitles')
        print('\r')

        for subtitle in subtitles:
            title_count += 1
            print(f'Subtitle {title_count}: {subtitle.text}\r')
            content = subtitle.find_next_sibling()
            content_text = ""

            while content and content.name != "h3":
                if content.name in ["p", "ul"]:
                    content_text += content.get_text(separator="\n") + "\n\n"
                content = content.find_next_sibling()

            subtitles_data[subtitle.text] = content_text.strip()

        print('\r')
        print('--Results alternate scraping--')
        print(f'Count of subtitles: {title_count}')

        for title in soup.find_all('title'):
            title_webpage = title.get_text()


        with open(f"data/{title_webpage}.json", "w", encoding="utf-8") as f:
            json.dump(subtitles_data, f, ensure_ascii=False, indent=4)

        # handling other features
        sentiment_func(title_webpage)
        detect_lang(title_webpage)
        load_analysis(title_webpage)


# standard webscraping function
def webscrape(url):

    response = requests.get(url)
    title_count = 0
    subtitles_data = {}

    if response.status_code == 200:
        print('[log] Webscraping running...')
        soup = BeautifulSoup(response.text, "html.parser")
        subtitles = soup.find_all("h2")
        print('[log] found all subtitles')
        print('\r')

        for subtitle in subtitles:
            title_count += 1
            print(f'Subtitle {title_count}: {subtitle.text}\r')
            content = subtitle.find_next_sibling()
            content_text = ""

            while content and content.name != "h2":
                if content.name in ["p", "ul"]:
                    content_text += content.get_text(separator="\n") + "\n\n"
                content = content.find_next_sibling()

            subtitles_data[subtitle.text] = content_text.strip()

        if title_count < 2:
            alternate_scrape(url)
        else:

            print('\r')
            print('--Results--')
            print(f'Count of subtitles: {title_count}')

            for title in soup.find_all('title'):
                title_webpage = title.get_text()


            with open(f"data/{title_webpage}.json", "w", encoding="utf-8") as f:
                json.dump(subtitles_data, f, ensure_ascii=False, indent=4)

            
            # handling other features
            sentiment_func(title_webpage)
            detect_lang(title_webpage)
            load_analysis(title_webpage)


    else:
        print("[Error 1] Error while calling website")