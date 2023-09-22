def busca(setor,m):
    matriz=[]
    i=0
    for  i in range(len(m)):
        if setor.lower( ) in matriz[i][0].lower( ):
            matriz.append(m[i][2:]+m+[1][3:])
    return matriz