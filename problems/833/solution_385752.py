def conta_numero(n:int,m:list)->int:
    x=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==n:
                x+=1
    return x