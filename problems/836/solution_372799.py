def busca(setor,matriz):
    ''''''
    i=0
    resul=[]
    while i<len(matriz):
        if setor in matriz[i][0]:
            resul=resul+[matriz[i]]
        i=i+1
    return resul