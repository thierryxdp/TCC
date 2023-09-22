def busca(setor,matriz):
    registro=[]
    
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            a=list.remove(matriz[i],matriz[i][2])
            registro+=a
    return registro