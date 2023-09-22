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
    frase.resersed(-1)
    return frase