def faltante(L):
    '''
    função que recebe uma lista L de tamanho N-1 contendo números inteiros
    de 1 a N e retorna um número inteiro que está faltando na lista
    list->int
    '''
     
    if 1 not in L:
        return 1
    
    Nfaltante = 0
    proximo = 0
    
    while proximo < (len(L)-1):
        
        if L[proximo]!= L[proximo + 1] - 1:
            Nfaltante = Nfaltante + (proximo + 2)
        proximo = proximo + 1
        
    if Nfaltante == 0:
               return L[-1] + 1
            
    return Nfaltante