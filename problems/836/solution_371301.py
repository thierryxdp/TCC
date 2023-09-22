def busca(Procurar, matriz):
    '''Dado uma area, retorna pessoas que estao habilitadas: str, list -> list'''
    lista = []
    contador = -1
    for linha in range(len(matriz)):
        if Procurar in matriz[linha]:
            for coluna in matriz[linha]:
                contador += 1
                if contador < 3:
                    lista += [coluna]
                if contador == 2:
                    lista = lista
            	
    return lista