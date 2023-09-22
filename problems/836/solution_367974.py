def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista_return = []
    i = 0
    j = 0
    while i < len(matriz):
        for j in matriz[i]:
            if setor == j:
                matriz[i].pop(2)
                list.append(lista_return, matriz[i]
        i + 1
        return lista_return