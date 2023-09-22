def uppCons(frase):
    consoante = []
    i = 0
    while i < len(frase):
        if consoante in 'b, c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z':
            frase = consoante.upper()
    return consoante