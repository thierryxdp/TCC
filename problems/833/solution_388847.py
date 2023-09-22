def conta_numero(numero,matriz):
    """int, list(list) -> int"""
    """retorna quantas vezes o número aparece na mstriz"""
    
    c = 0
    
    for i in matriz:
        c += list.count(i,numero)
        pass
    
    return c