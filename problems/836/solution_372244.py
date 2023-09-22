def busca(s,m):
    l=[]
    res=[]
    for i=m[3]:
        for j in range len(m[0]):
            if j == s:
                l=l+[j]
    for a in l:
        res=res+[m[0][a],m[1][a],m[3][a]]