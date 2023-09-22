import string
def conta_frases(frase):
    punct = string.punctuation
    for c in punct:
        frase = frase.replace(c, " ")
        final= len(frase.split('.'))
    return final