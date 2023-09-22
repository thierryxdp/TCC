def busca(setor,matriz):
    '''dado o setor e a matriz, retorna os dados do funcionário
    string, lista(lista) -> lista(lista)'''
    funcionarios = []
    for i in range(len(matriz)):
        funcionario = []
        for j in matriz[i][2]:
            if setor in j:
                list.append(funcionario, j)
        list.append(funcionarios, funcionario)
    return funcionarios