def qnt_divisores(n):
    ''' 
    recebe um inteiro e retorna quantos divisores ele tem
    int->list
    '''
    qnt=0
    for i in range(n):
        if n%i==0:
            qnt=qnt+1
    return qnt