def retira_pontuacao(frase):
    d = { '.': ' ', ':' : ' ', ';' : ' ', '-' : ' ', ',' : ' ', '?' : ' ', '!' : ' '}
    for c in d:
        frase =  str.replace(frase, c, d[c])
    return frase
def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = list(frase)
    frase = list.reverse(frase)
    frase = str(frase)
    frase = str.join(',' ,frase)
    return frase