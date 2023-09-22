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
    
    m=str.lower(frase)
    a=str.split(m)
    b=list.reverse(a)
    
    return a