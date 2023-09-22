def busca(setor, matriz):
    ''' Dado um setor da empresa, a função retorna os dados de todos os
        funcionarios do mesmo setor'''
    for i in matriz:
        if setor in i:
            return i