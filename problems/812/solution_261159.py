def retira_pontuacao(frase):
    """ funcao que dada uma frase, substitua todos os espacos 
    em branco por ” ”.
    """
    frase = frase.replace(","," ")
    frase = frase.replace("."," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("."," ")
    return frase