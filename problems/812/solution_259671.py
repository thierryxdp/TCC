def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a frase sem pontuação.
    str-> str"""
  
    if frase.split("."):
    	frase == ' '.join(frase.split("."))
    if frase.split("!"):
    	frase == ' '.join(frase.split("!"))
    if frase.split("?"):
    	frase == ' '.join(frase.split("?"))
    if frase.split(","):
    	frase == ' '.join(frase.split(","))
    if frase.split("..."):
    	frase == ' '.join(frase.split("..."))
    if frase.split("-"):
    	frase == ' '.join(frase.split("-"))
    return frase.split(" ")