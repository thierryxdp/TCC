def busca(setor,matriz):
    'dado o nome do setor e uma matriz, retorna os dados dos funcionarios daquele setor. str, list -> list'
    lista = []
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if (setor == matriz[i][j]):
                lista = [lista + [matriz[i][0],matriz[i][1],matriz[i][3]]
    return lista