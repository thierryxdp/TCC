def busca(x,matriz):
    """Função que recebe uma matriz e uma busca por um setor e retorna
    os dados de todos os funcionários daquele setor;lista,lista-->lista"""
    cont=[]
    for i in range(len(matriz)):
        if x==(matriz[i][2]):
            cont.append(matriz[i][:2]+[matriz[i][-1]])
    return cont