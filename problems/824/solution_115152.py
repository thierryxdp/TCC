def uppCons(texto):
    indice=0
    while indice<len(texto):
        if texto[indice] in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,z':
            texto_novo = str.upper(texto[indice])
            return texto_novo
        indice=indice+1
    return texto_novo