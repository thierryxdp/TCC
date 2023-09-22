def busca(setor,matriz):
    '''Recebe uma matriz que cpntém informações referentes a nomes,
    registo, setor e telefone de um funcionário e, ao receber um nome
    de um setor da empresa, retorna os dados de todos os funcionários 
    do mesmo.
    lista -> lista'''
    
    informacoes=[] 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][2]==setor:
                del matriz[i][2]
                lista = matriz[i]
                informacoes.append(lista)
    return informacoes