def qtd_divisores(num):

    '''
    funcao que recebe um numero e retorna quantos divisores esse numero tem
    int -> int
    '''
    i =  1
    divisor = 0    
    for i in range(1,num+1):
        if num%i == 0:
            divisor += 1
    i += 1
    return divisor