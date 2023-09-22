def media_matriz(mat):
    tam=(len(mat)*(len(mat[0])))
    total=0
    for i in mat:
        for j in i:
            total+=j
    med=total/tam
    return round(med,2)