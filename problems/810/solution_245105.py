def inverte(frase):
    """
    Retorna uma frase sem letras maiusculas, sem pontuacao e na ordem 
    inversa da que foi escrita inicialmente;
    str -> str
    """
    
    frase = frase.replace('.',' ') 
    frase = frase.replace('...',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('?',' ') 
    frase = frase.replace('!',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('-',' ')
    frase = frase.lower()
    frase = list(frase)
    return frase