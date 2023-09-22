def conta_frases(frase):
    '''
    Parametros: frase
    entrada: str
    saída  : int
    Funçao que conta quantas frases existem num texto
    
    '''
    
    if '...' in frase:
        frase = frase.replace('...','.')
    
    a= frase.count('.')
    b = frase.count('?')
    c = frase.count('!')

    return a+b+c