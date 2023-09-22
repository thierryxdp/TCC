def qtd_divisores(n):
    '''Retorna a quantidade de divisores que determinado número 'n' possui
       int -> int'''
    divisor = 0
    
    for valor in range(n+1) :
        if valor != 0:
            if n % valor == 0:
                divisor += 1
    
    return divisor