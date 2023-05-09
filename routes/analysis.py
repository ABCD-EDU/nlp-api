from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import store_topic_results, store_sentiment_results
from loaders.sentiment_model import perform_sentiment_analysis
from loaders.topic_model import perform_topic_modelling

router = APIRouter()

@router.post("/")
async def analyze_text(id:int,text: str):
    # Perform sentiment analysis
    sentiment_result = perform_sentiment_analysis(text)
    store_sentiment_results(id,sentiment_result)

    # Perform topic modelling
    topics_scores, topN_topics = perform_topic_modelling(text)
    store_topic_results(id,topics_scores )

    # Create a formatted response
    
    response_data = {
       "text": text,
        "sentiment_analysis": sentiment_result,
        "topic_modelling": topN_topics
    }

    return response_data
    # return JSONResponse(content=response_data)
