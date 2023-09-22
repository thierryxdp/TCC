def faltante(L):
    '''
    ex: [1,2,3,4,5,6]
    	
    '''
    if 1 not in L:
        return 1
        
    Nfaltante=0
    proximo=0
    
    while proximo<(len(L)-1):
        if L[proximo]!=L[proximo+1]-1:
            Nfaltante=Nfaltante+(proximo+2)
        proximo=proximo+1
    return Nfaltante

	Nfinal=0
    proximo2=0

	while proximo<(len(L)-1):
        if L[proximo2]==L[proximo2+1]-1:
            Nfinal=Nfinal+L[-1]+1
        proximo2=proximo2+1
    return Nfinal