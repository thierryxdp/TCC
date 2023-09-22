def busca(setor,matriz):
    ''''''
    lista1=[]
    lista2=[]
    lista3=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                lista1=[matriz[i][0]]
                lista2=[matriz[i][1]]
                lista3=[matriz[i][3]]
    return [lista1+lista2+lista3]