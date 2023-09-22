def qtd_divisores(n):
    ''' função que recebe um numero inteiro n e retorna quantos
        divisores ele possui
        int->int
        '''
    divisores=0
    for i in range(n):
        if n%(i+1)==0:
            divisores=divisores+1
    return divisores