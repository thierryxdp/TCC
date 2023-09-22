def qtd_divisores(n):
    """função que conte quantos divisores um numero tem, este numero sera passado como entrada 
    int -> int"""
    contador=0
    for divisor in range(1,n+1):
        if n%divisor == 0: 
    		contador= contador + 1 
        return contador