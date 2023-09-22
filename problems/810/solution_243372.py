def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '-', ' ')
    return frase
def inverte(frase):
    """inverte a ordem das palavras da frase dada."""
    frase2 = list.reverse(frase)
    return frase2