def inverte(frase):
    '''retorna a frase dada na ordem inversa'''
    '''str -> str'''
    
    frase=frase.replace('.',' ')
    frase=frase.replace('/',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('!',' ')
    
    sp= frase
    
    str.lower(frase)
    
    return frase[-1:]