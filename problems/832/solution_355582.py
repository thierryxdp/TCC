def eh_quadrada(m):
    if len(m)!= len(m[0]):
        return False
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            if m[i][j]!=m[j][i]:
                return False
            return True