def busca(setor,matriz):
    '''dado o setor e a matriz, retorna os dados do funcionário
    string, lista(lista) -> lista(lista)'''
    funcionarios = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(funcionarios, matriz[i])
    return funcionarios