def qtd_divisores(numero):
    '''Função que conta quantos divisore tem um determinado número'''
    'int ----> int'
    numero_divisor = numero%2==0
    i=0
    divisores=int()
    while i < numero :
        if i <= numero :
            divisores=divisores+(numero%numero_divisor==0)
            i=i+1
       
        i=i+1
    return (divisores)