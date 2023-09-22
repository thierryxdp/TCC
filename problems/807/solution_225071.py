import string
def conta_frases(frase):
    punct = string.punctuation
    for c in punct:
        frase = len(str(frase.replace(c, " "))) 
    return frase