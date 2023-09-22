def busca (setor,matriz):
    lista=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            setor=matriz[i][2]
            if setor in range(len(matriz)):
        lista=matriz[i][setor]
    return lista