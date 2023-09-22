def qtd_divisores(n):
    '''função que conta quantos divisores o numero n tem. o numero é passado como entrada. int -> int'''
    soma = 0
    for d in range(1,n+1):
        if n % d == 0:
            soma = soma + 1
    return(soma)