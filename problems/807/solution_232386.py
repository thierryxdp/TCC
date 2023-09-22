def conta_frases(texto) :
    """str -> int"""
    """recebe um texto e conta a quantidade de frases que tem nele"""
    
    C1 = texto.count('. ')
    C2 = texto.count('...')
    C3 = texto.count('?')
    C4 = texto.count('!')
    
    C = C1 + C2 + C3 + C4
    
    return C