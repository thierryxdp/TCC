def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
	
    frase = []
    
    if frase.split("."):
    	return ' '.join(frase.split("."))
    if frase.split("!"):
    	return ' '.join(frase.split("!"))
    if frase.split("?"):
    	return ' '.join(frase.split("?"))
    if frase.split(","):
    	return ' '.join(frase.split(","))
    if frase.split("..."):
    	return ' '.join(frase.split("..."))
    if frase.split("-"):
    	return ' '.join(frase.split("-"))
    return frase.split(" ")