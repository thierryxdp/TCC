def retira_pontuacao(frase):
    """Funcao que dada uma frase  retorna a mesma com todos os 
    caracteres de pontuacao sendo substituidos por espaco;str->str"""
	frase=frase.replace("-"," ")    
	frase.replace("."," ")
    frase.replace(","," ")
    frase.replace("-"," ")
    frase.replace(":"," ")
    frase.replace(";"," ")
    frase.replace("!"," ")
    frase.replace("?"," ")
    return frase