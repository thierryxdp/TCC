def inverte (frase):
    '''...'''
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    
    minuscula = str.lower(frase)
    Lista_palavra = str.split(minuscula)
    Lista_inversa = Lista_palavra[::-1]
    
    return str.join (' ', Lista_inversa)