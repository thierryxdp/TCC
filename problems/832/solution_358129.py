def eh_quadrada(matriz):    
    nLinhas = len(matriz)
    nColu = len(matriz[0])
    if nLinhas == nColu:
        print("A matriz fornecida é quadrada!")
    else:
        print("A matriz fornecida não é quadrada!")