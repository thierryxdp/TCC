def inverte(frase):
    """
    Retorna uma frase sem letras maiusculas, sem pontuacao e na ordem 
    inversa da que foi escrita inicialmente;
    str -> str
    """
    frase = frase.lower
    frase = frase.replace('.',' ') 
    frase = frase.replace('...',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('?',' ') 
    frase = frase.replace('!',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('-',' ')
    
    return frase