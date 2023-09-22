def busca(setor,matriz):
    '''retorna os dados dos funcionarios do setor especificado
    str, list(list) -> list(list)'''
    dados = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            cadastro = matriz[i]
            dados += [cadastro[0:2] + [cadastro[3]]]
    return dados