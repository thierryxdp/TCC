def soma_h(n):
    """Dado um número n, retorna o valor da soma dado por H. int -> int"""
    soma = 0
    for i in range(1,n+1):
        soma = soma + 1/i
    return round(soma,2)