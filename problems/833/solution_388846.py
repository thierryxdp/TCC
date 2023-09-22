def conta_numero(numero,matriz):
    """int, list(list) -> int"""
    """retorna quantas vezes o número aparece na mstriz"""
    
    c = 0
    
    for i in matriz:
        if numero in i:
            c += 1
            pass
        pass
    return c