def fatorial(num):
    '''
       Função que recebe um numero inteiro (num) e retorna
       o fatorial desse numero;
       int->int
    '''
    i=0
    a=0
    while i<num:
        num=num*i+a
        i=i+1
    return num