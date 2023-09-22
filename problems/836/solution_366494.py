def busca(funcao,matriz):
    """ recebe uma matriz que cada linha é a informação de um funcionário e, ao fazer a busca de uma função, retorna quem está naquele cargo e as informações"""
    funcionarios=[]
    for dados in range(len(matriz)):
        if matriz[dados][2]==fucao:
            list.remove(matriz[dados],fucao)
            list.append(funcionarios,matriz[dados])
    return funcionarios