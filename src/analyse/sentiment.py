import json
from textblob import TextBlob

def sentiment_func(file):
    with open(f'data/{file}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key in data:
        text = data[key]
        sentiment = TextBlob(text).sentiment.polarity
        data[key] = {'sentiment': round(sentiment, 3)}

    with open(f'informations/infos.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)