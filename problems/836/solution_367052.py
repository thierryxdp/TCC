def busca(nome,matriz):
    """Para fazer uma busca, com base em um setor da
    empresa, e retornar os dados de todos funcionários
    daquele setor, digite;
    matriz->matriz"""
    cont=[]
    for i in range(len(matriz)):
        for j in matriz[i][2]:
            del(matriz[j][2])
            cont+=[matriz[j]]
    return cont