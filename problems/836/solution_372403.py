def busca(string,matriz):
    '''Função que recebe uma string e uma matriz ,onde o número de
    linhas depende da quantidade de funcionários,em que cada linha 
    tem 4 entradas referentes ao nome, registro, setor e telefone
    de um funcionário, respectivamente,e faça uma busca por setor, 
    ou seja, dado o nome de um setor da empresa, a função retorna
    uma lista com os dados de todos os funcionários daquele setor.
    str,list(list)->list'''
    resposta=[]
    for i in range(len(matriz)):
        linha=[]
        if matriz[i][2]==string:
            linha.append(matriz[i][0])
            linha.append(matriz[i][1])
            linha.append(matriz[i][2])
            linha.append(matriz[i][3])
            resposta.append(linha)
    return resposta