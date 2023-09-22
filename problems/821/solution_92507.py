def fatorial(numero):
    '''Função que, dado um número, calcula seu fatorial. int -> int'''
    multiplica = 1
    for i in range(1, (numero+1)):
        multiplica = multiplica * i  
    return multiplica