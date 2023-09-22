def qtd_divisores(numero):
    '''Função que conta quantos divisore temum determinado número'''
    'int ----> int'
    
    numero_divisor = numero%2==0
    i=0
    while i % numero == 0:
        print (numero_divisor)
        i=i+1