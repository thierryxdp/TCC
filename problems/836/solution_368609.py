def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        if str.upper(matriz[i][2]) == str.upper(setor):
            local = list.remove(matriz[i],matriz[i][2])
            lista += local
    return lista