def busca(setor,matriz):
    lista=[]
    tam=0
    for i in (len(matriz)):
            if setor in i:
                lista.append([matriz [tam][0],matriz[tam][1],matriz[tam][3]])
            tam+=1

    return lista