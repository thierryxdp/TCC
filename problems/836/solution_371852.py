def busca(setor,matriz):
    '''Função que ao receber uma matriz que contém o nome do
    funcionário, registro, setor e telefone do funcionário
    faz uma busca por setor me retornando os dados de todos
    os funcionários daquele mesmo setor.
    str,list ->str'''
    a=0
    b=0
    quero=[]
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a=a+1
            if matriz[i][j]==setor:
                append=lista.append(matriz[i])
                lista.remove(setor)
            else:
                lista
    return lista