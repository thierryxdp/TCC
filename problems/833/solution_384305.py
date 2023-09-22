def conta_numero(numero,matriz):
    """ Essa função conta quantas vezes o numero 
    esta na matriz. matriz,int->int."""
    for i, elem in enumerate(lista):
        menor = elem
        for k, elem in enumerate(lista[index:]):
            if elem < menor:
                lista[k+i] = menor
                menor = elem
        lista[i] = menor
    return lista