def soma_h(n):
    """funçao que calcula e retorna o valor de H com N termos one N é inteiro e dado com entrada;int,int->int"""
    soma = 0.0
    for i in range(1, n + 1):
        soma = soma + 1 / i
    return round(soma, 2)