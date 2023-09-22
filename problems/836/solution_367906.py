def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista = []
    lista_return = []
    acum = 0
    while acum < len(matriz):
        if setor in matriz[acum][2]:
            lista += matriz[acum]
            list.remove(lista, setor)
            lista_return += lista
        acum + 1
        return lista_return