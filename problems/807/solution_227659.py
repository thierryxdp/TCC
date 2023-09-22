def conta_frases(frase):
    '''função que conta frases permitindo uso de reticencias, 
    interrogações e exclamação apenas no final delas'''
    return len(str.split(frase,['...','!','?'])