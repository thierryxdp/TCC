def soma_h(n):
    """A funçao retorna a soma de n termos com 1/n, sendo n um inteiro de 1 a n.int --> float"""
    soma = 0
    for i in range(1,n + 1):
        soma = soma + 1/i
    return round(soma,2)