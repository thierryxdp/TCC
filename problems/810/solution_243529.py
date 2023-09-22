def inverte(frase):
    """
    	Retorna a frase em ordem invertida, sem potuação e com leras minúsculas.
        str -> str
    """
    frase=frase.replace(',',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=frase.lower()
    frase=frase.split()
    frase=' '.join(reversed(frase))
    return frase