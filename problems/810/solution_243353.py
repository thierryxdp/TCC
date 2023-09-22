def retira_pontuacao (frase):
    """ retira as pontuações especiais e coloca espaço."""
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, ',', '')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '-', ' ')
    return frase
def inverte(frase):
    """inverte a ordem das palavras da frase dada."""
    for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
    return new_string