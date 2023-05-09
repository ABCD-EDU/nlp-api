import os
from sqlalchemy import create_engine, text
from util.db import client

def store_topic_results(post_id,topic_values):
  col_names = " ".join([f"topic{i}," for i in range(0,15)])[:-1]
  values = " ".join([f"{i}," for i in topic_values])[:-1]
  statement = text(f"INSERT INTO topic_scores (post_id, {col_names}) VALUES ({post_id}, {values})")
  client.session.execute(statement)
  client.session.commit()
  print('added topic scores')

def store_sentiment_results(post_id,sentiment_values):
  statement = \
    text(f"INSERT INTO sentiment_scores (post_id, positive, negative, neutral) VALUES ({post_id}, {sentiment_values['positive']}, {sentiment_values['negative']}, {sentiment_values['neutral']})")

  client.session.execute(statement)
  client.session.commit()
  print('added sentiment scores')

def fetch_metrics():
    pass

