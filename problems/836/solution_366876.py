def busca(setor,matriz):
    lista=[]
    indice1=0
    while indice1<len(matriz):
        indice2=0
        while indice2<len(matriz[0]):
            if matriz[indice1][indice2]==setor:
                list.append(lista,matriz[indice1][0])
            indice2=indice2+1
        indice1=indice1+1
    return lista