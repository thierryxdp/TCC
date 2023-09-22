def qtd_divisores(n):
    '''
    Recebe um inteiro positivo n e retorna sua quantidade de divisores
    
    int -> int
    '''
    i=0
    for d in range(1,n):
        if n%d==0:
        	i=i+1
    return i