def conta_frases(frase):
    '''função que conta a quantidade de frases.
    split()'''
    
    list = (frase.split('.'))
    list = (frase.split('!'))
    list = (frase.split('?'))
    list = (frase.split('...'))
    
    return len(list)