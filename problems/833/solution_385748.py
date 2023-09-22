def conta_numero(n:int,m:list):
    x=0
    for i in len(m):
        for j in len(m[i]):
            if m[i][j]==n:
                x+=1
    return x