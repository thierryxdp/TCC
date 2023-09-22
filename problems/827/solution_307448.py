def qtd_divisores(n):
    ''' 
    recebe um inteiro e retorna quantos divisores ele tem
    int->list
    '''
    q=0
    for i in range(n):
        if n%i==0:
            q=q+1
    return q