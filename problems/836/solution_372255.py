def busca(s,m):
    l=[]
    res=[]
   
    for j in range (len(m)):
            if m[j][2] == s:
                res=res+[m[j][0],m[j][1],m[j][3]]
    return res