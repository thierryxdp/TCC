def media_matriz(matriz):
    """calcula a media dos elementos de uma matriz;
    matriz, -> int"""
    
    m = matriz
    c = 0
    d = 0
    
    for i in range(len(m)):
        a = m[i]
        b = sum(a)
        c = c + b
        d = d + len(a)
    return sort(c/d)