def busca(setor,matriz):
    """ A funcao busca, recebe uma matriz como a do exemplo e faz uma busca por setor, ou seja, dado um nome de um setor da empresa, 
 a funcao retorna os dados de todos os funcionarios daquele setor.
 list --> lis """
    resultado = []
    nlin = len(matriz)
    if nlin == 0:
        return resultado
    ncol = len(matriz[0])
    for i in range(nlin):
        if setor in matriz [i][2]:
            lista = []
            list.append(lista,matriz[i][0])
            list.append(lista,matriz[i][1])
            list.append(lista,matriz[i][3])
            
    return resultado