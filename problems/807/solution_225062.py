import string
def conta_frases(frase):
    punct = string.punctuation
    for c in punct:
        frase = str(frase.replace(c, " "))
        final= len(frase.split('.'))+len(frase.split('?'))+len(frase.split('!'))
    return final