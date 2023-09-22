def busca(matriz,nomesetor):
    'dada uma matriz, busque o nome do setor da empresa e retorne os dados de todos os funcionários daquele setor.list(list),str-->list'
    func=[]
    for i in range(len(matriz)):
        if matriz[i][2]==nomesetor:
            f=matriz[0:2]+[3:]
            list.append(func,f)
    return func