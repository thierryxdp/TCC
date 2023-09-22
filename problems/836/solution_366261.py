def busca (setor, matriz):
    '''Retorna uma lista contendo os dados inseridos em uma matriz (nome, registro, setor e telefone) de um funcionário em base do setor inserido;
    str, list -> list'''
    matriz_nova = []
    para_acrescentar = []
    linhas = len(matriz)
    
    for i in range(linhas):
        if matriz[i][2] == setor:
            para_acrescentar.append(i)
    count = 0
    
    for i in para_acrescentar:
        matriz_nova.append(matriz[i])
        count += 1
    
    for i in range(len(matriz_nova)):
        matriz_nova[i].remove(setor)
    return matriz_nova