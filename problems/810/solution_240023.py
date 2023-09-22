def inverte(frase):
    """A função 
    
    Entrada: String
    Saída: String"""
    
    minus = str.lower(frase)
    dividir = str.split(minus,(',','!','?','.',',','-'))
    frase_invertida = dividir
    
    return frase_invertida