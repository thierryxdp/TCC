def uppCons(frs):
    ''' '''
    i=0
    consoantes = ''
    while i<len(frs):
        if frs[i]=='b, c, d, f, g, j, k, l, m, n, p, q, r, s,t,v,w, x,z':
           consoantes+= str.upper(frs[i])
        i+=1
    return consoantes