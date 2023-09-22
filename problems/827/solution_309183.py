def qtd_divisores(numero):
    '''Função que conta quantos divisore tem um determinado número'''
    'int ----> int'
    i=0
    numero_divisor = numero%2==0
    par=int()
    divisores=int()
    
    while i < numero :
        i=i+1
        divisores=divisores+(numero%i==0)
    i=i+1
    return (divisores)