def busca(setor,matriz):
    ''' função que recebe uma matriz e faça uma busca por setor, ou seja, dado um nome de um setor da empresa, a função retorna os dados de todos os funcionários daquele setor.
    Entrada: list, str;
    Saída: list'''
    acumulador = [ ]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(acumulador,matriz[i])
        list.remove(acumulador[2],setor)
    return acumulador