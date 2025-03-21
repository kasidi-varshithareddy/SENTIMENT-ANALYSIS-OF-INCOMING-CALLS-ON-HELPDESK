from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive", "😊", polarity
    elif polarity < 0:
        return "Negative", "😡", polarity
    else:
        return "Neutral", "😐", polarity

if __name__ == "__main__":
    sample_text = "I am very happy with the service!"
    sentiment, emoji, score = get_sentiment(sample_text)
    print(f"Text: {sample_text}\nSentiment: {sentiment} {emoji}\nScore: {score:.2f}")
