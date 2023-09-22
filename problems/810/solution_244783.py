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
    
    str.lower(sp)
    
    return sp[-1:]