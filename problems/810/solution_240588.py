def inverte(frase):
    """Funcao que recebe uma string (frase) e retorna a sua
    forma na ordem inversa.
    str -> list"""
   
    pontuacao = "-,.:;?!"
	
    for p in pontuacao:
        frase = frase.replace(p, " ")
        
    transformador_lista = frase.split()
    invertedor = transformador_lista[::-1]
    frase_invertida = " ".join(invertedor)
    
    return frase_invertida