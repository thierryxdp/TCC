def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    frase = str.replace(frase, '!', '')
    frase = str.replace(frase, '?', '')
    frase = str.replace(frase, ',', '')
    frase = str.replace(frase, ':', '')
    frase = str.replace(frase, ';', '')
    frase = str.replace(frase, '.', '')
    frase = str.replace(frase, '-', '')
    return frase
def inverte(frase):
    str.split(frase)
    return frase