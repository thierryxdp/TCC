def busca(matriz,setor):
    '''Funçao que busca as pessoas de um setor;
    Recebe uma matriz com dados dos funcionários;
    Retorna uma lista com os funcionários do setor pedido.'''
    lista = []
    for elemento in matriz:
        if matriz[2] == setor:
            lista += matriz[0] + matriz[1]+ matriz[3]
    if lista != []:
        return lista
    else:
        return lista