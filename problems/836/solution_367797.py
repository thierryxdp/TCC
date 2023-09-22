def  busca(setor, matriz):
    '''Retorna uma lista de funcionários que trabalha no setor informado.
    list -> list'''
    lista = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            del matriz[i][2]
            list.append(lista,matriz[i])
    return lista