def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ', frase)
    return frase