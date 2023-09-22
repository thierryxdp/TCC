def retira_pontuacao(frase):
    """ funcao que dada uma frase, substitua todos os espacos 
    em branco por ” ”.
    """
    frase = str.split(frase, ",")
    frase = str.join(frase, ".")
    frase = str.join(frase, "-")
    frase = str.join(" ", frase)
    return frase