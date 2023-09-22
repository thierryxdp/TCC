def qtd_divisores(n):
    '''Conta quantos divisores tem um numero;
    int -> int'''
    contador = 0
    divisores = list(range(1,n+1))#lista com numeros de 1 a n
    divisor = 0 #numero que dividira n
    for divisor in divisores:
        if n % divisor == 0:
           contador = contador + 1 
    return contador