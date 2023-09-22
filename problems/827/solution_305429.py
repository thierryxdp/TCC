def qtd_divisores(n):
    """função que conte quantos divisores um numero tem, este numero sera passado como entrada 
    int -> int"""
    contador=0
    i=0
    for divisor in range(1,n+1):
        if n%i == 0: 
            i = i+1
    		contador = contador + 1 
        return contador