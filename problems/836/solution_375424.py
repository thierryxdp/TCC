def busca(matriz,setor):
    '''Funçao que busca as pessoas de um setor;
    Recebe uma matriz com dados dos funcionários;
    Retorna uma lista com os funcionários do setor pedido.'''
    lista = []
    for elemento in matriz:
        if elemento[2] == setor:
            lista += elemento[0] + elemento[1]+elemento[3]
    if lista != []:
        return lista
    else:
        return lista