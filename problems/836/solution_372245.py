def busca(s,m):
    l=[]
    res=[]
   
    for j in range len(m[2]):
            if m[2][j] == s:
                l=l+[j]
    for a in l:
        res=res+[m[0][a],m[1][a],m[3][a]]