def busca(Procurar, matriz):
    '''Dado uma area, retorna pessoas que estao habilitadas: str, list -> list'''
    lista = []
    for linha in range(len(matriz)):
        if Procurar in matriz[linha]:
            lista += [matriz[linha]]
            lista[indice].index(Procurar)
    return lista