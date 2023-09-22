def melhor_volta(m):
    g=()
    d=[]
    for i in range(6):
        for n in range(10):
            list.append(d,m[i][n])
    for i in range(len(m)):
        for n in range(len(m[0])):
            if m[n][i]==min(d):
                    g=d+(n)+(i)
    return (g[0],min(d),g[1])