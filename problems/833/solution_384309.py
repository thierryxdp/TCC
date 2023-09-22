def conta_numero(elem,matriz):
    """ Essa função conta quantas vezes o numero 
    esta na matriz. matriz,int->int."""
    for i, elem in enumerate(matriz):
        menor = elem
        for k, elem in enumerate(matriz[i:]):
            if elem < menor:
                matriz[k+i] = menor
                menor = elem
        matriz[i] = menor
    return elem