def retira_pontuacao(tweet):
    import string
    translator = string.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
    x = tweet.translate(translator)
    return x