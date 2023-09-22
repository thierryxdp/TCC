def quant_palavras(frase):
   """recebe uma frase e retorna o numero de palavras nela contidas
    string -> int"""
    
	palavras = str.split(frase)
    
    if (frase[0] == ' ' or frase[-1] == ' '):
        return len(palavras)
    
    elif (frase[0] == ' ' and frase[-1] == ' '):
        return len(palavras) - 1
    
    else:
        return len(palavras)