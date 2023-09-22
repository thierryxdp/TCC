def busca(setor, matriz):
    '''funcao que dada uma matriz e o nome de um setor, retorna as informações de todos os funcionarios daquele setor
       string, matriz(strings) -> list(strings)'''
    lista = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(matriz[i], lista)
    return lista