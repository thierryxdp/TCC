def retira_pontuacao(frase):
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    return frase
def inverte(frase):
    frase = str.lower(frase)
    frase = retira_pontuacao(frase)
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ',frase)
    return frase