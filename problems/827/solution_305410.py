def qtd_divisores(n):
    """função que conte quantos divisores um numero tem, este numero sera passado como entrada 
    int -> int"""
    for divisor in range(1,n+1):
        if n%divisor == 0: 
    print(divisor)