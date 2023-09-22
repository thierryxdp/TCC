def inverte(frase):
    
    """essa função inverte as palavras de uma frase qualquer;
       str->str"""
    frase = frase.replace(',',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('-',' ')
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ',(frase))
    frase = str.lower(frase)
    return frase