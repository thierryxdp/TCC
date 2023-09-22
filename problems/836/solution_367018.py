def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        for setor in matriz[i][2]:
            if setor in matriz[i][2]:
                lista+=matriz[i]
                i+=1
            return lista