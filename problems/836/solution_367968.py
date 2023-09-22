def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista = []
    lista_return = []
    i = 0
    j = 0
    while i < len(matriz):
        for j in matriz[acum1]:
            if setor == j:
                lista += matriz[acum1]
                list.pop(lista[acum1], setor)
                lista_return += lista
        i + 1
        return lista_return