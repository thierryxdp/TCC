def inverte(frase):
    """função que dada uma frase, retorna a mesma frase de entrada, só que na ordem inversa, sem maiúsculos ou pontuação
	str -> str"""
    
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace("...", " ")
    
    frase = str.split(frase)
    frase.reverse()
    frase = str.join(" ", frase)
    frase = str.lower(frase)
    
    return frase