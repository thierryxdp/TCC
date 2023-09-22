def busca(Procurar, matriz):
    '''Dado uma area, retorna pessoas que estao habilitadas: str, list -> list'''
    lista = []
    for linha in range(len(matriz)):
        if Procurar in matriz[linha]:
            lista += [matriz[linha]
           	for indice in range(len(lista)):
                if lista[indice] == Procurar:
                      lista[indice].remove(Procurar)
            	
    return lista