def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista = []
    lista_return = []
    acum1 = 0
    for i in matriz:
        acum2 = 0
        for j in matriz[acum1]:
            if setor == matriz[acum1][acum2]:
                lista += matriz[acum1]
                list.remove(lista, setor)
                lista_return += lista
            acum2 += 1
        acum1 + 1
        return lista_return, acum1, acum2