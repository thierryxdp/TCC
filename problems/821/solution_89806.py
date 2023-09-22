def fatorial(num):
    '''
       Função que recebe um numero inteiro (num) e retorna
       o fatorial desse numero;
       int->int
    '''
    i=0
    while i<=num:
        fat=num*i
        fat=fat+num*i
        i=i+1
    return fat