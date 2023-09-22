def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        if str.upper(matriz[i][2]) == str.upper(setor):
            local = list.remove(matriz[i],setor)
            lista = list.extend(lista,local)
    return lista