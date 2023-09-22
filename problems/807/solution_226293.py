def conta_frases(texto):
    """
    dado uma string contendo um texto, retorna seu número de frases.
    """
    
    x= str.replace(texto,'.','')
    x= str.replace(x,'!','')
    x= str.replace(x,'?','')
    
    z=str.split(x)
    
    return len(z)