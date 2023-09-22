def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista = []
    lista_return = []
    acum1 = 0
    while acum1 < len(matriz):
        acum2 = 0
        for j in matriz[acum1]:
            if setor == j:
                lista += matriz[acum1]
                list.remove(lista, setor)
                lista_return += lista
        acum1 + 1
        return lista_return