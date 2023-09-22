def uppCons(frase):
    cons = [q,w,r,t,y,p,s,d,f,g,h,j,k,l,ç,z,x,v,n,m]
    indice = 0
    while indice < len(frase):
        if cons in frase:
          d =  str.replace(frase,cons,str.upper(cons))
    return d