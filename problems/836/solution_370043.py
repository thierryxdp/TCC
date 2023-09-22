def busca(setor,matriz):
    '''função recebe uma matriz com infos sobre um funcionário e um setor de trabalho e reTorna todos os funcionários que trabalham nesse setor E SUAS INFOS.LIST,STR->LIST'''
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            fun=funcionario
            fun.remove(funcionario[2])
            result.append(fun)
    return result