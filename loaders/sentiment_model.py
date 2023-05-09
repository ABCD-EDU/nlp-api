# import loaders.model.sentiment.modifiedVaderSentiment SentimentIntensityAnalyzer as SentimentIntensityAnalyzer

from loaders.model.sentiment.modifiedVaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
   
def _clean_output(input_data):
   output = {}
   for key,value in input_data.items():
      if key=='pos':
         output['positive'] = value
      if key=='neg':
         output['negative'] = value
      if key=='neu':
         output['neutral'] = value
   return output
         
def perform_sentiment_analysis(text:str):
   return _clean_output(analyzer.polarity_scores(text))
   