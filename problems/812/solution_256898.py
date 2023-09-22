def retira_pontuacao(tweet):
    import re
    clean = re(r"[,.;@#?!&$]+\ *", " ", tweet)
    return clean