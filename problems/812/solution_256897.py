def retira_pontuacao(tweet):
    import re
    clean = re.sub(r"[,.;@#?!&$]+\ *", " ", tweet)
    return clean