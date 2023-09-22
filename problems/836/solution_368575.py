def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista_return = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor == matriz[i][2]:
                matriz[i].pop(2)
                list.append(lista_return, matriz[i])
    return lista_return