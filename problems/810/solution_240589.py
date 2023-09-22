def inverte(frase):
    """Funcao que recebe uma string (frase) e retorna a sua
    forma na ordem inversa.
    str -> list"""
   
    pontuacao = "-,.:;?!"
	
    for p in pontuacao:
        frase = frase.replace(p, " ")
        
    transformador_lista = frase.split()
    invertedor = transformador_lista[::-1]
    transformador_string= " ".join(invertedor)
    frase_invertida = transformador_string.lower
    
    return frase_invertida