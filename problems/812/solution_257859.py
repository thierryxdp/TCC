def retira_pontuacao(frase):
    """função que dada uma frase, retorna a mesma só que substituindo os caracteres de pontuação por espaço
	str -> str"""
    
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace("...", " ")
    
    return frase