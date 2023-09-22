def busca(setor, matriz):
    '''função que dados um setor e matriz, retorne os dados dos funcionários deste setor. str, list -> list'''
    lista = 0
     acum1 = 0
    for i in matriz:
        acum2 = 0
        for j in matriz[acum]:
            if setor == matriz[acum1][acum2]:
                list.append(matriz, matriz[acum1])
        return lista