def busca(Procurar, matriz):
    '''Dado uma area, retorna pessoas que estao habilitadas: str, list -> list'''
    lista = []
    for linha in matriz:
        if Procurar in linha:
            lista += [linha]
            lista[0].remove(Procurar)	
    return lista