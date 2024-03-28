import requests
import wikipedia
from loguru import logger
from bs4 import BeautifulSoup
from config.config import wiki_url
from deep_translator import GoogleTranslator


def categories_words(topic):
    # Obtain Wikipedia categories related to the given topic
    topics = wikipedia.search(topic)
    return topics


def fetch_wikipedia_info(topic):
    """
    Fetches information about the given topic from Wikipedia.

    Parameters:
    - topic (str): The topic to search for on Wikipedia.

    Returns:
    - title (str): The title of the Wikipedia page.
    - article_text (str): The text content of the Wikipedia page.
    """
    try:
        # Construct URL for the selected topic on English Wikipedia
        url = f"{wiki_url}{topic.replace(' ', '_')}"

        # Fetch content from the Wikipedia page
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1", {"id": "firstHeading"}).text
        content_div = soup.find("div", {"id": "mw-content-text"})

        if content_div:
            article_text = content_div.text.strip()  # Strip whitespace from the text
            if article_text:  # Check if article_text is not empty after stripping whitespace
                # Translate the content to English
                translated_text = translator_text(article_text)
                logger.info(f"Translated text: {translated_text}")
                return title, translated_text
            else:
                print("Content found on the page, but it is empty.")
                return None, ""
        else:
            print("Content not found on the page.")
            return None, ""
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None, ""


def translator_text(text):
    """
    Translates the given text to English using Google Translator.

    Parameters:
    - text (str): The text to translate.

    Returns:
    - translated_text (str): The translated text.
    """
    # Initialize translated text
    translated_text = ""

    try:
        # Instantiate GoogleTranslator object
        translator = GoogleTranslator(source='auto', target='en')

        # Split text into chunks of maximum length 5000 characters
        max_chunk_size = 2000
        chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

        # Translate each chunk and concatenate the results
        translated_chunks = [translator.translate(chunk) for chunk in chunks]
        translated_text = " ".join(translated_chunks)
    except Exception as e:
        print("Translation error:", e)

    return translated_text.strip()  # Strip leading/trailing whitespace





