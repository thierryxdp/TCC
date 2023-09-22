def uppCons(frase):
    '''uppCons recebe uma frase e devolve a frase com todas as suas consoantes em maiuscula.
    str-->str'''
    i=0
    frase1=list(frase)
    while i<len(frase):
        if frase1[i] in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,y,x,z,ç':
            frase1[i]=str.upper(frase1[i])
        i=i+1
    return ''.join(frase1)