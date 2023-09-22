def busca(string,matriz):
    cont=[]
    a=len(matriz)
    b=len(matriz[0])
    for i in range(a):
        for j in range(b):
            if string in matriz[i][2]:
                del(matriz[i][2])
                cont=cont+[matriz[i]]
                if string in matriz[j][2]:
                    del(matriz[j][2])
                    cont=cont+[matriz[i][j]]
            
        

    return cont