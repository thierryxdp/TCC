def busca(setor, matriz):
    ''' Função que busca as informações de funcionários de um determinado setor da empresa
    str, list -> list '''
    lista = []
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[i]))):
            if matriz[i][j] == setor:
                list.append(lista, matriz[i])
                list.remove(lista[j])
    return lista