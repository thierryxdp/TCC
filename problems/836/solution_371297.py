def busca(Procurar, matriz):
    '''Dado uma area, retorna pessoas que estao habilitadas: str, list -> list'''
    lista = []
    contador = 0
    for linha in range(len(matriz)):
        if Procurar in matriz[linha]:
            for coluna in matriz[linha]:
                if contador < 3:
                    lista += [coluna]
       			contador += 1
            	
    return lista