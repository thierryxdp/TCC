def  busca(setor, matriz):
    '''Retorna uma lista de funcionários que trabalha no setor informado.
    list -> list'''
    lista = []
    for i in range(len(matriz)):
        matriz1 = matriz[i][0]+matriz[i][1]+matriz[i][3]
        if matriz[i][2] == setor:
            list.append(lista,matriz1[i])
    return lista