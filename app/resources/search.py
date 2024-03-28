import wikipedia
from typing import List
from fastapi import Query
from loguru import logger
from init import searching_router
from information_wikipedia.info import fetch_wikipedia_info, categories_words

@searching_router.get("/search/", response_model=List[str])
def search_topics(query: str = Query(..., title="Query", description="Enter the search query")):
    """
    Search Wikipedia for topics related to the given query.
    """
    topics = categories_words(query)
    return topics


@searching_router.get("/fetch/")
def fetch_info(topic: str = Query(..., title="Topic", description="Enter the topic to fetch information")):
    """
    Fetch information about the given topic from Wikipedia.
    """
    try:
        info = fetch_wikipedia_info(topic)
        if info[0] and info[1]:
            return {"title": info[0], "content": info[1]}
        else:
            raise HTTPException(status_code=404, detail=f"No information found for topic: {topic}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
