def busca(setor,matriz):
    '''função que dada uma matriz e um setor de escolha retorne os funcionários daquele setor desejado
    sendo as variáveis, setor uma string que informa o setor e matriz uma lista com informações de funcionários'''
    fun=[]
    for i in matriz:
        for j in i:
            if j==setor:
        return fun