def retira_pontuacao(frase):
    """
    	string -> string
    """
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    return frase