def eh_quadrada(matriz):
    "Identifica se uma matriz é quadrada ou nao, dado: uma matriz."
    
    l= 0
    c= 0
    for x in matriz:
           l += 1
           c = len(x)
    return l == c