def uppCons(frase):
    '''Recebe uma frase a analisa o parâmetro de entrada e retorna todas 
    as consoantes encontradas em maiúsculas e os demais caractéres no formato original
    tupla -> tupla'''
    
    consoantes = ('B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z,b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z')
    i = 0
    lista = ()
    
    
    
    while i < len(frase):
        if frase[i] in consoantes:
            frase[i].upper()
            lista = lista + str.(frase[i])
    i = i + 1
    return frase