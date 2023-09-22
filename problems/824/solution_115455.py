def uppCons(frase):
    '''
        recebe uma frase e retorna a mesma frase, porem, com todas as consoantes
        maiusculas e os demais caracteres inalterados
        entrada: string
        saida: string
    '''
    chq = 0
    frase_modf = ''
    consoantes = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,X,Z'
    while chq<len(frase):
        if frase[chq] in consoantes:
            frase_modf = frase_modf + str.upper (frase[chq])
        else:
            frase_modf = frase_modf + frase[chq]
        chq = chq + 1
    return frase_modf