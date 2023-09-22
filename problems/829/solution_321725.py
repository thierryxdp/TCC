def soma_h(n):
    """Função que calcula  a soma  como un inteuro como base
    int -> int"""
    soma = 0
    for i in range(1 , n+1):
        soma = soma + float(1//n)
    return round (soma, 2)