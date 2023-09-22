def busca(area, lista):
    """funcao que recebe uma matriz e faz a busca por area de todos os funcionarios do setor;
    str,list->list"""
    matriz = []
    for i in range(len(lista)):
        info = []
        for j in range(len(lista[0])):
            if lista[i][j] == area:
                list.append(info, lista[i][0])
                list.append(info, lista[i][1])
                list.append(info, lista[i][3])
        if info != []:
            list.append(matriz, info)
    return matriz