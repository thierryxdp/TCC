def soma_h(n):
    """Retorna o valor H com N termos, onde N é inteiro e dado como entrada"""
    soma = 0
    for i in range (1,n+1):
        soma += 1.0/i
    return round(soma,2)