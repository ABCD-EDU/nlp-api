from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
import numpy as np
import os


current_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(current_dir, 'model','topic', 'topic_model_mmr')


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
topic_model = BERTopic.load(file_path, embedding_model=embedding_model)

topics = ['General', 'Parks and Recreation', 'Traffic Management', 'Waste Management', 'Housing', 'Public Safety', 'Infrastructure', 'Healthcare', 'Tourism and Travel Destinations','Food', 'Environment', 'Arts and Culture', 'Community Development',
         'Taxes Budget and Finance', 'City Ordinances']

topic_dict = {i: topic for i, topic in enumerate(topics)}


def _get_topN_topics(input_data):
   # Get indices of the top 5 highest elements
   top_indices = np.argsort(-input_data)[:5]
   topN_topics = []
   for i in top_indices:
      topN_topics.append(topic_dict[i])
   return topN_topics


def _clean_output(input_data): 
   _, topics_score = input_data
   arr = np.array(topics_score[0])
   topics_scores = np.round(arr, 5)
   topN_topics = _get_topN_topics(arr)
   topic_numbers = [f"topic{i}" for i in range(0,15)]
   topics_scores_ ={} 
   for topic_number, topic_score in zip(topic_numbers, topics_scores):
      topics_scores_[topic_number] =  topic_score
   return topics_scores_, topN_topics

def perform_topic_modelling(text:str):
   return _clean_output(topic_model.transform(text))