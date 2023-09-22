def conta_numero(numero, matriz):
    """Função que retorna quantas vezes o numero aparece na matriz
    int, list--> int"""
    a=matriz
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if a[i][j]==numero:
                list.append(lista,1);
            else:
                list.append(lista,0);
    return lista.count(1)