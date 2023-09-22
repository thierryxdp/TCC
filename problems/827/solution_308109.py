def qtd_divisores(n):
    '''
    Função que conta quantos divisores um dado numero 
    inteiro tem.
    
    int-->int
    '''

    lista=0 
    for i in range(1,n+1):
        if n % i== 0:
            lista=lista+1
            
    return lista