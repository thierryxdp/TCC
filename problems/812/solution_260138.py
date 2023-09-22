def retira_pontuacao(frase):
    """."""
    lista = ["," , ":" , ";" , "." , "-"]
	for n in frase: frase.replace(n, ' ')
    nova_frase = frase.replace(n, ' ')