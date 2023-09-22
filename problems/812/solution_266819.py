def retira_pontuacao(pal):
    d = { '.': ' ', ':' : ' ', ';' : ' ', '-' : ' ', ',' : ' ', '?' : ' ', '!' : ' '}
    for x in d:
        pal =  str.replace(pal, x, d[x])
    return pal
def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ', frase)
    return frase