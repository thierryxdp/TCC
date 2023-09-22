def conta_frases(texto):
    count = lambda l1,l2: sum([1 for x in l1 if x in l2])
    return count(texto,set(texto.punctuation))