def uppCons(frase):
    """Retorna uma frase com todas as suas consoantes em maiúsculas; string -> string."""
    i = 0
    while i < len(frase):
        if frase[i:i+1:] in "b,c,d,f,g,j,k,l,m,n,p,q,r,s,t,v,w,x,z":
            str.replace(frase,frase[i:i+1:],str.upper(frase[i:i+1:]),1)
            i= i + 1
    return frase