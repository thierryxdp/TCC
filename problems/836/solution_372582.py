def busca(setor,matriz):
    '''Recebe uma matriz e retorna o resultado de uma busca por dados
    de funcionarios de um determinado setor
    list -> dic'''
    y = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            y = y + [matriz[i]]
            return y