from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import store_results
from loaders.sentiment_model import perform_sentiment_analysis
from loaders.topic_model import perform_topic_modelling

router = APIRouter()

@router.post("/")
async def analyze_text(id:int,text: str):
    # Perform sentiment analysis
    sentiment_result = perform_sentiment_analysis(text)
   #  store_sentiment_results("sentiment_analysis", sentiment_result)

    # Perform topic modelling
    topic_result = perform_topic_modelling(text)
   #  store_results("topic_modelling", topic_result)

    # Create a formatted response
    response_data = {
       "text": text,
        "sentiment_analysis": sentiment_result,
        "topic_modelling": topic_result
    }

    return response_data
    # return JSONResponse(content=response_data)
