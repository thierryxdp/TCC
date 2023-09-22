def uppCons(frs):
    ''' '''
    i=0
    consoantes = ''
    while i<len(frs):
        if frs[i]in 'b, c, d, f, g, j, k, l, m, n, p, q, r, s,t,v,w, x,z':
           consoantes=str.upper(frs[i])
        elif frs[i]in'a,e,i,o,u':
            consoantes+=str.lower(frs[i])
        elif frs[i]in'A,E,I,O,U':
            consoantes+=str.upper(frs[i])
        i+=1
    return consoantes