import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

english_stopwords = stopwords.words("english")
analyzer = SentimentIntensityAnalyzer()

def get_levels(entry):
    scores_list = []
    pattern = re.compile(r'[A-Za-z]+')
    words = re.findall(pattern, entry)

    d = {}
    for word in words:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1
    
    d_list = [(value, key) for (key, value) in d.items()]
    d_list.sort(reverse = True)

    filtered_words = []
    for count, word in d_list:
        if word not in english_stopwords:
            filtered_words.append((word, count))
    
    scores = analyzer.polarity_scores(entry)
    scores_list.append(scores)
    
    return scores_list