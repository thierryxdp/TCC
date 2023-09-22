def retira_pontuacao(frase):
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    return frase
def inverte(frase):
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    return frase