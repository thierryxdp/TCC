def qtf_divisores(n):
    'Funçao que conta quantos divisores um numero tem'
    soma = 0
    
    for d in range(1,n+1):
        if n % d == 0:
            soma = soma + 1
    return soma