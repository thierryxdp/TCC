def bolos(xicara=2, ovos=3, colheres=5):
    '''calcula a quantidade de bolos de uma determinada receita,
    dado a quantidade de xícaras de trigo, ovos e colheres de leite, respectivamente.
    Por padrão, as entradas estão configuradas para atender a quantidade para fazer 1 bolo.'''
    import math
    
    A = math.floor(xicara/2)
    B = math.floor(ovos / 3)
    C = math.floor(colheres /5)
    bolo = A + B + C / 3
    
    return math.floor(bolo)
    
    return