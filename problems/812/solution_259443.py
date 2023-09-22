def retira_pontuacao(frase):
    """  """
    frase=[ ]
    if frase(".", "-",".,",",",":",";","!","?","...","_",".;"):
        return " "
	else:
        return str(frase)