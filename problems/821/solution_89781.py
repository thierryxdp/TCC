def fatorial(num):
    '''
       Função que recebe um numero inteiro (num) e retorna
       o fatorial desse numero;
       int->int
    '''
    i=0
    while i<=num:
        i=i+1
        num=num*(i)
    return num