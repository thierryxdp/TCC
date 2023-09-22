def busca(setor, matriz):
    '''função que recebe uma matriz com dados de funcionários de
    uma empresa e um nome de um setor e retorna os dados de todos
    os funcionários da empresa que trabalham naquele setor'''
    resultado = []
    for i in range(len(matriz)):
        pessoa = matriz[i]
        if setor in matriz[i]:
            pessoa.remove(setor)
            resultado.append(pessoa[:])
    return resultado