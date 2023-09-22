def busca(setor, matriz):
    '''funcao que dada uma matriz e o nome de um setor, retorna as informações de todos os funcionarios daquele setor
       string, matriz(strings) -> list(strings)'''
    resultado = []
    j = 0
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            lista = []
            list.append(lista, matriz[i][0])
            list.append(lista, matriz[i][1])
            list.append(lista, matriz[i][3])
            resultado[0][j] = lista
            j += 1
    return lista