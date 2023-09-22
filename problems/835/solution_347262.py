def melhor_volta(m):
    nlin = len(m)  
    ncol = len(m[0])
    for i in range(nlin):
        if i == 1:
            rmin = min(m[i-1])
            ri = i
            for j in range(ncol):
                if m[i-1][j-1] == rmin:
                    rj = j
        testmin = min(m[i-1])
        if testmin <= rmin:
            rmin = testmin
            ri = i
            for j in range(ncol):
                if m[i-1][j-1] == rmin:
                    rj = j
    return ri,rmin,rj