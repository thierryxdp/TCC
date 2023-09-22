def conta_numero(numero,matriz):
    ''' '''
    lista=[]
    m=matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if m[i][j]==numero:
                list.append(lista,1)
            else:
                list.append(lista,0)
    return lista.count(1)