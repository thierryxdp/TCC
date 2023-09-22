def busca(Procurar, matriz):
    '''Dado uma area, retorna pessoas que estao habilitadas: str, list -> list'''
    lista = []
    for linha in range(len(matriz)):
        if Procurar in matriz[linha]:
            lista += [matriz[linha]]
            a = lista.index(Procurar)
            lista.remove(a)
    return lista