def busca(setor,matriz):
    '''função que dada uma matriz e um setor de escolha retorne os funcionários daquele setor desejado
    sendo as variáveis, setor uma string que informa o setor e matriz uma lista com informações de funcionários'''
    fun=[]
    a=[]
    for i in matriz:
        for j in i:
            if j==setor:
                a.append(i[0])
                a.append(i[1])
                a.append(i[3])
                b=[a]
                fun.append(b)
    return fun