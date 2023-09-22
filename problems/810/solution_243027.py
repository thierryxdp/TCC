def inverte(frase):
    """
    
    	string -> string
    """
    frase = frase.lower()
    frase = frase.replace('.',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.split()
    frase.reverse()
    return frase