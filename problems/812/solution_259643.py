def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
   	
    frase=f1
	
    if f1.split("."):
    	return ' 'join(f1.split("."))
    if f1.split("!"):
    	return ' 'join(f1.split("!"))
    if f1.split("?"):
    	return ' 'join(f1.split("?"))
    if f1.split(","):
    	return ' 'join(f1.split(","))
    if f1.split("..."):
    	return ' 'join(f1.split("..."))
    if f1.split("-"):
    	return ' 'join(f1.split("-"))
    return f1.split(" ")[::-1]