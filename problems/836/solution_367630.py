def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
            if setor in i:
                lista.append([matriz[0],matriz[1],matriz[3]])
    return lista