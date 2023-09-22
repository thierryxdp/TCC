def busca(s,m):
    l=[]
    res=[]
   
    for j in range (len(m[2])):
            if m[2][j] == s:
                res=res+[m[0][j],m[1][j],m[3][j]]
    return res