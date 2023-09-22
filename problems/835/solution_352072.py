def melhor_volta(mat):
    lista1 = []
    lista2 = []
    for i in range(len(mat)):
        lista1.append(min(mat[i]))
        lista2.append(mat[i].index(min(mat[i])))
    tempo = lista1.index(min(lista1))
    volta = lista2[tempo]
    mat1  = list(range(0,6))
    vencedor = mat1[tempo]
    return (vencedor+1, min(lista1),volta+1)