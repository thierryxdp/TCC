def eh_quadrada(m):
    total = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            total = total + 1
        if len(m)-len(m[0])==0:
            return True
        if len(m)-len(m[0])!=0:
            return False
        else:
            return True