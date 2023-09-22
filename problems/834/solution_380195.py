def media_matriz(m):
    cont = 0
    i = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            cont += m[i][j]
   	num = len(m[i])*len(m)
    div = cont/num
    
    return round(div,2)