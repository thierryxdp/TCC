def conta_frases(frase):
    '''função que conta frases permitindo uso de reticencias, 
    interrogações e exclamação apenas no final delas'''
    a= str.split(frase,'?')
    b = str.split(frase,'!')
    c = str.split(frase,'...')
    return len(c)