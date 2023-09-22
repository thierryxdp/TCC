def faltante(lista):
    n = len(lista)
    soma1 = sum(range(1, n + 1))
    soma2 = sum(lista)
    
    k = soma1 - soma2
    
    return k