def busca(setor,matriz):
    '''função que dada uma matriz e um setor de escolha retorne os funcionários daquele setor desejado
    sendo as variáveis, setor uma string que informa o setor e matriz uma lista com informações de funcionários'''
    fun=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            fun=fun+[matriz[i]]
    return fun