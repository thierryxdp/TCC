def retira_pontuacao(frase):
    """Retorna a frase sem pontuacao.str-->str."""
    return str.replace(frase,"!"," ")
	return str.replace(frase,"-"," ")
	return str.replace(frase,":"," ")
	return str.replace(frase,";"," ")
	return str.replace(frase,"?"," ")
	return str.replace(frase,"."," ")