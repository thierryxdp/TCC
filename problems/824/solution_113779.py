def uppCons (frase):
    """ transforma todas as consoantes da frase em maiúsuclas"""
    list(frase)
    consoantes = list.index (b,c,d,f,g,h,j,k,l,m,n,o,p,q,r,s,t,v,w,x,y,z)
    str(consoantes)
    cons_up = str.upper (consoantes)
    str.replace (frase, consoantes, cons_up)
    return frase