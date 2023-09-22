def uppCons(frase):
    lista=list(frase)
    cosoantes=""
    i=0
    while i<len(frase):
        if lista[i] in "b,c,d,f,g,j,k,l,m,n,p,q,r,s,t,v,w,x,z":  
        	lista[i]=str.upper(lista[i])
        i=i+1
    return str(lista)