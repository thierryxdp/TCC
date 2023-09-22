def busca(string,matriz):
    '''Uma função recebe uma string do nome de um setor da empresa e uma matriz
    com os dados de funcionários de uma empresa e retorna os dados de todos os
    funcionários daquele setor.
    str, list -> list'''
    resultado_busca=[]
    for i in range(len(matriz)):
            if str.upper(matriz[i][2])==str.upper(string):
                del matriz[i][2]
                resultado_busca=resultado_busca+[matriz[i]]
    return resultado_busca