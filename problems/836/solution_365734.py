def busca(setor,matriz):
    '''dado o setor e a matriz, retorna os dados do funcionário
    string, lista(lista) -> lista(lista)'''
    funcionarios = []
    for i in range(len(matriz)):
        funcionario = []
        for j in range(len(matriz[0])):
            if setor in j:
                list.append(funcionario, matriz[i])
        list.append(funcionarios, funcionario)
    return funcionarios