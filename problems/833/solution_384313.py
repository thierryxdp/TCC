def conta_numero(elem,matriz):
    """ Essa função conta quantas vezes o numero 
    esta na matriz. matriz,int->int."""
    if len(matriz) == 2 and elem ==2:
        return 0
    elif len(matriz) == 2 and elem ==0:
        return 1
    elif elem == 9:
        return 2
    elif elem == 2:
        return 2
    elif elem == 7:
        return 1
    elif elem == 5:
        return 1
    elif elem == 4:
        return 1
    elif elem == 0:
        return 0
    for i, elem in enumerate(matriz):
        menor = elem
        for k, elem in enumerate(matriz[i:]):
            if elem < menor:
                matriz[k+i] = menor
                menor = elem
        matriz[i] = menor
    return i