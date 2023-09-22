def busca (s,m):
    r=[]
    
    for i in range(len(m)):
        for j in range (len(m[0])):
            if s in str(m[i][j]):
                r+=[m[i]]
    for i in range(len(r)):
        tamanho=len(r[i])-1
        for j in range(tamanho):
            if r[i][j]==s:
                del r[i][j]
    return r