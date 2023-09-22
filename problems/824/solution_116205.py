def uppCons(x):
    '''A função retorna as consoantes em maiúscula (caso houver) e os demais
    caractéres como estava na frase original
    str -> str'''
    
    y = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'
    
    z = 0
    w = ''
    
    while len(x) > z:
        if x[z] in y:
            w = w + str.upper(x[z])
        if x[z] not in y:
            w = w + x[z]
        z = z + 1
        
    return w