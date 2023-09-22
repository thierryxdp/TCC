def uppCons(frase):
    """Retorna uma frase com todas as suas consoantes em maiúsculas; string -> string."""
    i = 0
    frase2 = frase
    while i < len(frase2):
        if frase2[i:i+1:] in "b,c,d,f,g,j,k,l,m,n,p,q,r,s,t,v,w,x,z":
            str.replace(frase2,frase2[i],str.upper(frase2[i]),1)
            i= i + 1
        else:
            i= i + 1
    return frase2