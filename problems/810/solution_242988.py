def inverte(frase):
    """
    
    	string -> string
    """
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    return frase[::-1]