def retira_pontuacao(frase):
    d = { '.': ' ', ':' : ' ', ';' : ' ', '-' : ' ', ',' : ' ', '?' : ' ', '!' : ' '}
    for c in d:
        frase =  str.replace(frase, c, d[c])
    return frase
def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = list(frase)
    frase = list.split(frase)
    frase = list.inverse(frase)
    frase = str.join(frase)
    return frase