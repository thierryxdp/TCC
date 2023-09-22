def primos(n):
    """Função que diz se um numero é primo ou não
    int -> bool"""
    for c in range(1 , n+1):
        if n % c ==0:
            return 'True'
        else:
            return 'False'