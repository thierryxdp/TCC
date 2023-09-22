def conta_frases(x):
    '''a função recebe um texto e retorna o numero de frases que aparecem no texto
    assinatura: str -> int
    casos de teste:
    '''

    x1 = str.count(x, '.')
    x2 = str.count(x, '!')
    x3 = str.count(x, '?')
    x4 = str.count(x, '...')
    
    return x1 + x2 + x3 + x4