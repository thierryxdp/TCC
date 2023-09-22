def conta_numero(numero,matriz):
    ''' int, list --> int'''
    
    resultado = 0
    for l in matriz:
        for c in l:
            if c == numero:
                resultado += 1
    return resultado