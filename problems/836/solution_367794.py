def  busca(setor, matriz):
    '''Retorna uma lista de funcionários que trabalha no setor informado.
    list -> list'''
    lista = []
    matriz1=matriz[0]+matriz[1]+matriz[3]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(lista,matriz1[i])
    return lista