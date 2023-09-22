def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        if str.upper(matriz[i][2]) == str.upper(setor):
            lista += matriz[i][0:2] + [matriz[i][3]]
    return lista