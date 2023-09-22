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
    frase.split(' ')
    return frase