def busca(matriz,setor):
    '''Esta função retorna os dados de um funcionário em uma lista, fazendo uma busca na matriz dada.
list,str->list'''
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                list.append(lista,([matriz[i][0],matriz[i][1],matriz[i][3]]))
    return lista