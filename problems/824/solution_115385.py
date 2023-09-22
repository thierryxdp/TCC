def uppCons(frase):
    ''' ''' 
    i=o
    while i<len(frase):
        if frase[i] in 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, y, w, z':
            l=frase[i]
            maiusculo=str.upper(l)
            frase=str.replace(frase,l,maiusculo)
            i+=1
            return frase