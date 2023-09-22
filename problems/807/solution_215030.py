def conta_frases(texto):
    """Dá a quantidade de frases em um texto
    	str -> int
    	Parameters:
        texto: Texto a ser analisado
        
        Returns:
        Quantidade de frases presentes no texto
    """
    
    contador = str.count(texto,'...')
    frase = texto.replace('...',' ')
    contador = contador + str.count(frase,'!')
    frase = frase.replace('!', ' ')
    contador = contador + str.count(frase,'?')
    frase = frase.replace('?', ' ')
    contador = contador + str.count(frase,'.')
    frase = frase.replace('.',' ')
    
    return contador