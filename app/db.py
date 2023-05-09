from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text, insert
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float
from sqlalchemy.orm import sessionmaker
load_dotenv()


POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DATABASE')
POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine=create_engine(f"{POSTGRES_URL}")
# Define the metadata for the tables
metadata = MetaData()

# Define the sentiment_scores table schema
sentiment_scores_table = Table(
    'sentiment_scores',
    metadata,
    Column('post_id', Integer, primary_key=True),
    Column('positive', Float),
    Column('negative', Float),
    Column('neutral', Float)
)

# Define the topic_scores table schema
topic_scores_table = Table(
    'topic_scores',
    metadata,
    Column('post_id', Integer, primary_key=True),
    *[Column(f'topic{i}', Float) for i in range(0, 15)]
)


# Create session factories for sentiment scores and topic scores
SentimentSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
TopicSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def store_topic_results(post_id,topic_values):
    with engine.connect()  as con:
        stmt = topic_scores_table.insert() \
            .values(
                post_id=post_id,
                **topic_values
            )
        con.execute(stmt)
        con.commit()
        print('added topic scores')

def store_sentiment_results(_post_id,sentiment_values):
    # print(f"{(**sentiment_values)}")
    with engine.connect() as con:

        # insert_statement = """
        # INSERT INTO sentiments_scores (post_id, positive, negative, neutral)
        # VALUES(:post_id, :positive, :negative, :neutral)
        # """
        stmt = sentiment_scores_table.insert().values(
            post_id=_post_id,
            **sentiment_values
        )
        con.execute(stmt)
        con.commit()
        
def fetch_metrics():
    pass

