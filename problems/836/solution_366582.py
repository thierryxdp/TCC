def busca(string,matriz):
    '''Função que receba uma string e uma matriz e faça uma busca por setor, ou seja,
    dado o nome de um setor da empresa. retorna uma lista com os dados de todos os
    funcionários daquele setor. str, list -> list'''
    dados = []
    for i in range(len(matriz)):
        if string in matriz[i]:
            a = matriz[i][2]
            list.remove(matriz[i],a)
            dados += [matriz[i]]
    return dados