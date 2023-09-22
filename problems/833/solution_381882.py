def conta_numero(numero,matriz):
    '''função que, dados um número inteiro e uma matriz de inteiros, conta e 
    retorna quantas vezes aquele número aparece na matriz; int, list -> int'''
    lista=[]
    m=matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if m[i][j]==numero:
                list.append(lista,1)
            else:
                list.append(lista,0)
    return lista.count(1)