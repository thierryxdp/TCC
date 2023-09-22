def busca(funcionario, matriz):
    '''Função que busca o nome de um setor da empresa e retorna os dados de todos os funcionários do setor, str, list -> list'''
    lista = []
    for i in range(len(matriz)):
        if funcionario == matriz:
            lista = lista + 1
    return lista