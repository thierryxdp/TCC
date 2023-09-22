def melhor_volta(m):
    nlin = len(m)  
    ncol = len(m[0])
    for i in range(nlin):
        if i == 0:
            rmin = min(m[i])
            ri = i
            for j in range(ncol):
                if m[i][j] == rmin:
                    rj = j
        testmin = min(m[i])
        if testmin < rmin:
            rmin = testmin
            ri = i
            for j in range(ncol):
                if m[i][j] == rmin:
                    rj = j
    return ri+1,rmin,rj+1