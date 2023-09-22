def uooCons(frase):
    ''' funcoa que recebe uma frase e retorna a frase com as consoantes em maiúscula
    str -> str'''
    consoante = 'b, c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'
    if frase.upper() in consoante:
        return (consoante)
    else:
        return frase