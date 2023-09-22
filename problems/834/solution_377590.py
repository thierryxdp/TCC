def media(x):
    c=[]
    n_linhas=len(x)
    n_cols=len(x[0])
    for i in range(n_linhas):
        for j in range(n_cols):
            c.append(x[i][j])
            
    return round((sum(c)/len(c)),2)