def busca(setor,matriz):
    ''''''
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                lista=lista+[matriz[i][0]]+[matriz[i][1]]+[matriz[i][3]]
    return lista