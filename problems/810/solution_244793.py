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
    
    a=str.lower(frase)
    b=str.join(reversed(a))
    
    return b