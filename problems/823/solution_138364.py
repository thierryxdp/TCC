def faltante(L):
    '''
    função que retorna a peça do quebra cabeça que está faltando. A função recebe uma lista L,
    que contem N-1 peças do quebra cabeça. Obs: As peças são numeradas de 1 a N.
    list->int
    '''
    
    if 1 not in L:
        return 1
        
    Nfaltante=0
    proximo=0
    
    while proximo<(len(L)-1):
        if L[proximo]!=L[proximo+1]-1:
            Nfaltante=Nfaltante+(proximo+2)
        proximo=proximo+1
    if Nfaltante==0:
               return L[-1]+1
            
    return Nfaltante