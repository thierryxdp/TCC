def melhor_volta(matriz):
    indice1=0
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    lista=[]
    while indice1<nlinhas:
        indice2=0
        while indice2<ncolunas:
            list.append(lista,matriz[indice1][indice2])
            indice2=indice2+1
        indice1=indice1+1
    
    quem=int(list.index(lista,min(lista))/10)+1
    return (quem, min(lista))