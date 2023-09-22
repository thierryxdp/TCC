def primo (n):
    '''função que dado um número inteiro n como entrada, verifica
    se ele é primo ou não, retornando um valor booleano'''
    contador=0
    for divisor in range (1,n+1):
        if n % divisor == 0:
            contador += 1
        
    if contador == 2:
    	'True'
    else:
    	'False'