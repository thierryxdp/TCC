def soma_h(n):
    """função na qual calcula e retorna o valor H com N termos"""
    soma = 0
    numero = 1
    for x in range(1,n + 1):
        soma += 1/numero
        numero += 1
    return round(soma,2)