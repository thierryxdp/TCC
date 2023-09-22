def busca(setor, matriz):
    '''Função que procura na matriz de funcionários de uma empresa um determinado setor.
    Retorna uma nova matriz de funcionários somente daquele setor.
       str, matriz ---> lista'''
    matriz_resposta = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            list.append(matriz_resposta,funcionario[:2] + funcionario[3:])
    if matriz_resposta != []:
        return matriz_resposta 
    return  'sei lá'