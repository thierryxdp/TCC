def busca(setor,matriz):
    '''Funcao que receba um setor e uma matriz, e
retorna os dados de todos os funcionarios daquele
setor'''
    funcionarios = []
    for linha in range(len(matriz)):
        if setor in matriz[linha]:
            list.remove(matriz[linha],setor)
            list.append(funcionarios,matriz[linha])
    return funcionarios