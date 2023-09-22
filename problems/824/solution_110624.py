def uppCons(frase):
    consoante = 'b, c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'
    while consoante in frase:
        if consoante.upper() in frase:
            return consoante
        else:
            return frase