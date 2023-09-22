def melhor_volta(m):
    maxi=[]
    maxi2=[]
    res=()
    
    for i in range(len(m)):
        maxi=[[max(m[i])] + [i]]
        
    for i in range(len(maxi)):
        for j in range(len(maxi[0])):
            
            maxi2 = max(maxi[i])
            
            if m[i][j] in maxi2:
                res = (i, m[i][j], j)
                
    return res