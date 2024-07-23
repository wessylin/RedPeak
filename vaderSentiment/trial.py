from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Analyze sentiment
text = input('Pleaase input the text you would like to analyze: ')

# text = "I love this product! It's amazing."
sentiment_scores = sid.polarity_scores(text)

print(sentiment_scores)
