def busca(setor,matriz):
    matriz=[]
    i=0
    for  i in range(len(matriz)):
        if setor.lower( ) in matriz[i][0].lower( ):
            matriz.append(matriz[i][2:]+matriz+[1][3:])
            i=i+''
    return matriz