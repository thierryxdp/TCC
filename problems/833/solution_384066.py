def conta_numero(numero,matriz):
    """conta quantas vezes um numero x aparece em uma matriz;
    int, matriz, -> int"""
    
    m = matriz
    n = numero
    c = []
    
    for i in range(len(m)):
        a = m[i]
        b = a.count(n)
        list.append(c, b)
    return c