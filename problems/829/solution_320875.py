def soma_h(n):
    """Calcula o valor de h com n termos inde n é inteiro; int -> int"""
    soma = 0
    for i in range(1, n+1):
        soma += (1/i)
    return round(soma,2)