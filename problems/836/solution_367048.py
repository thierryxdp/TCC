def busca(nome,matriz):
    """Para fazer uma busca, com base em um setor da
    empresa, e retornar os dados de todos funcionários
    daquele setor, digite;
    matriz->matriz"""
    cont=[]
    for i in range(len(matriz)):
        for nome in matriz[i][2]:
            del(matriz[i][2])
            cont+=[matriz[i]]
    return cont