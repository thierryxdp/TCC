def retira_pontuacao(frase):
    """ funcao que dada uma frase, substitua todos os espacos 
    em branco por ” ”.
    """
    frase = frase.split(frase, ",")
    frase = frase.replace(" ", frase)
    return frase