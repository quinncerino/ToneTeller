import re
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from random import choice

english_stopwords = stopwords.words("english")
analyzer = SentimentIntensityAnalyzer()


def get_sentences(entry):
    pattern = re.compile(r'[^.!?]+[.!?]')
    sentences = re.findall(pattern, entry)
    return sentences


def get_filtered_words(entry):
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
    
    return filtered_words


def get_sentence_levels(entry):
    sentences = get_sentences(entry)
    scores_list = [{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}]
    for sentence in sentences:
        score = analyzer.polarity_scores(sentence)
        scores_list.append(score)
    return scores_list


def get_words(score):
    very_positive = ["overjoyed", "ecstatic", "thrilled", "delighted", "elated", "jubilant"]
    positive = ["happy", "cheerful", "joyful", "optimistic", "encouraged", "pleased", "upbeat", "satisfied"]
    negative = ["sad", "upset", "worried", "frustrated", "discouraged", "disappointed", "downcast", "gloomy", "uneasy"]
    very_negative = ["devastated", "miserable", "depressed", "melancholy", "outraged", "resentful"]
    neutral = ["calm", "steady", "indifferent", "composed", "neutral", "matter-of-fact", "relaxed"]

    if (score >= 0.5):
        return choice(very_positive)
    elif (score >= 0.4):
        return choice(positive)
    elif (score <= -0.5):
        return choice(very_negative)
    elif (score <= -0.4):
        return choice(negative)
    else:
        return choice(neutral)
    
def get_emojis(score):
    if (score >= 0.5):
        return choice(["😆✨🥳🌈", "🌟🌸😊💫", "🌞🌈💖😆", "✨🦄🥳🌟", "💎🌞🎉🤩", "😍🌟🤩🎊", "☀️💫😇😍"])
    elif (score >= 0.4):
        return choice(["🤗👍🙂🍀", "🌻🌟💖😎", "😊✨🌸🌅", "😌🌹🌞💫", "🌟🍀😄🌼", "🏞️😌💫😎"])
    elif (score <= -0.5):
        return choice(["⚡😡💔🔥", "☠️😫🩸🕯️", "🌋💀😫⚡", "😠🔥💔🪦", "💔🌪️😤🕯️"])
    elif (score <= -0.4):
        return choice(["🥀🙁🌧️🌫️", "🕯️💀😕🌑", "🌧️📉😞🕸️", "😔🌙🌧️🕯️", "😓🌩️😟🌫️", "🌧️😔🥀💧"])
    else:
        return choice(["💤😐⚖️🌙", "🌔🧘🌀✨", "🕯️😴📖🌌", "😶🔮🌗📜", "🤔🌙🌀😐"])