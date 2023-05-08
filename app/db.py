from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
load_dotenv()


POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DATABASE')
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine=create_engine(f"{POSTGRES_URL}")


def store_topic_results(post_id,topic_values):
    with engine.connect()  as con:
        col_names = " ".join([f"topic{i}," for i in range(0,15)])[:-1]
        values = " ".join([f"{i}," for i in topic_values])[:-1]
        statement = text(f"INSERT INTO topic_scores (post_id, {col_names}) VALUES ({post_id}, {values})")
        con.execute(statement)
        print('added topic scores')

def store_sentiment_results(post_id,sentiment_values):
    with engine.connect() as con:
        statement = \
          text(f"INSERT INTO sentiment_scores (post_id, positive, negative, neutral) VALUES ({post_id}, {sentiment_values['positive']}, {sentiment_values['negative']}, {sentiment_values['neutral']})")
        
        con.execute(statement)
        print('added sentiment scores')
        
def fetch_metrics():
    pass

