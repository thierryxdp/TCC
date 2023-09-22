def busca(setor,funcionario):
    '''Recebe uma matriz e retorna o resultado de uma busca por dados
    de funcionarios de um determinado setor
    list -> dic'''
    l1 = []
    if setor in funcionario[0]:
        l1 = l1 + [funcionario[0]]
        l1[0].remove(setor)
        l1 = l1
        if setor in funcionario[1]:
            l1 = l1 + [funcionario[1]]
            l1[0].remove(setor)
            if setor in funcionario[2]:
                l1 = l1 + [funcionario[2]]
                l1[1].remove(setor)
                return l1