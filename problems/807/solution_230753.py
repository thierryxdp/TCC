def retira_pontuacao(frase):
    d = { '.': '.', '?' : '.', '!' : '.'}
    for c in d:
        frase =  str.replace(frase, c, d[c])
    return frase
def conta_frases(frase):
    frase = retira_pontuacao(frase)
    frase = str.split(frase, '.')
    frase = len(frase)
    return frase