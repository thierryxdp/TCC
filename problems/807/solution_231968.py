def conta_frases(x):
    p=['.','!', ' ... ', '?',';',':']
    for y in p:
        s=str.partition(x,y)
        return s