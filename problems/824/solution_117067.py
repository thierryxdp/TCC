def uppCons(frase):
    i=0
    consoantes=[b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z]
    while i<len(frase):
        if frase[i] in consoantes:
            frase[i]=str.upper(frase[i])
        i+=1
    return frase