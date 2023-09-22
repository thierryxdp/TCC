def eh_quadrada(m):
    b=[]
    c=[]
    for i in range (0,len(m)):
        for j in range (0,len(m[i])):
            b.append(j)
            c.append(i)
    if max(c, key=int)==max(b, key=int):
        return True
    else:
        return False