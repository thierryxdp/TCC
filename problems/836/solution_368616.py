def busca(setor,matriz):
    lista = []
    for i in range(len(matriz)):
        if str.upper(matriz[i][2]) == str.upper(setor):
            lista += matriz[i] 
    return lista