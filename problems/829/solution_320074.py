def soma_h(n):
    """Calcula a soma de frações de 1/2 até 1/n
       int ~> int"""
    soma = 0
    for num in range(1,n+1):
        soma += num**-1
    return round(soma,2)