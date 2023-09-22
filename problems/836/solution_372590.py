def busca(setor,matriz):
    '''Função que busca e retorna os dados de todos os funcionarios de determinado setor da empresa
    list -> dic'''
    y = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            y = y + [matriz[i]]
    return y