def busca(setor,matriz):
    lista=[]
    indice1=0
    while indice1<len(matriz):
        indice2=0
        while indice2<len(matriz[0]):
            if matriz[indice1][2]==setor:
                list.append(lista,matriz[indice2][0])
                list.append(lista,matriz[indice2][1])
                list.append(lista,matriz[indice2][3])
            indice2=indice2+1
        indice1=indice1+1
    return lista