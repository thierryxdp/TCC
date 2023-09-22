def busca(setor, matriz):

    """ Função que recebe uma string e uma matriz e faz uma busca por setor, ou seja, dado o nome de um setor da empresa,
    a função retorna uma lista com os dados de todos os funcionários daquele setor. Se nenhum registro for encontrado, a função
    retornará uma lista vazia."""

    lista = []
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
               lista.append([matriz[i][0], matriz[i][1], matriz[i][3]])    
    return lista