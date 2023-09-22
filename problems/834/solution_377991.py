def media_matriz(matriz):
    """função que dada uma lista matrix calcula a média de seus numeros;
    list->float"""
    x=0
    k=0
    for i in matriz:
        for j in i:
            x=x+j
            k=k+1
    return round(x/k,2)