def uppCons(frase):
    indice=0
    frase_nova = ''
    consoantes = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,z,B,C,D,F,G,H,J,L,M,N,P,Q,R,S,T,V,X,Z'    while indice<len(frase):
        if frase[indice] in consoantes == True:
            uppconsoante = str.upper(consoantes)
            return uppconsoante
            frase_nova = frase_nova + uppconsoante
        indice= indice+1    
        else:
            frase_nova+=frase[indice]
        indice = indice+1
    return frase_nova