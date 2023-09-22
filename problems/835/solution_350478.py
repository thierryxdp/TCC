def melhor_volta(m):
    l=[]
    for i in range (len(m)):
        for j in range (len(m[0])):
            l=l+[m[i][j]]
    a=min(l)
    b=l.index(a)
    return[(int(b/10))+1,a,(int(b%10))+1]