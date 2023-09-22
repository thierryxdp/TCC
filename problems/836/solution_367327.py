def busca (nome,matriz):
    '''Função faz uma busca por 'nome' na matriz de informações fornecidas.
    str, list -> list'''
    achou = []
    for i in range (len(matriz)):
        for j in range (4):
            if nome == matriz[i][j]:
                list.append (achou, matriz[i])
    for f in range (len(achou)):
        del achou[f][2]
    return achou