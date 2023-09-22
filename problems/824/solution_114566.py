def uppCons(frase):
    indice=0
    frase_nova=''
    consoantes = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,z'
    while indice<len(frase):
        if frase[indice] in consoantes == True:
            uppconsoante = str.upper(consoantes)
            return uppconsoante
        frase_nova = frase_nova + uppconsoante
        indice=indice+1       
    return frase_nova