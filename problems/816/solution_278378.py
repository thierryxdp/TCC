def maiores(x,y):
    media = sum(x)/len(x)
    if y in x:
        c = x.index(y)
        b = sorted(x)
        return b[c::]
    elif y not in x:
        e = [y]
        novalista = e + x
        novalista1 = sorted(novalista)
        c = novalista1.index(y)
        d = c + 1
        return novalista1[d::]