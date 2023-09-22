def soma_h (n):
    """Funcao para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada. Retorne seu resultado somente com 2 casas decimais, utilizando a função round(numero, 2).
    int -> float"""
    soma = 0
    for x in range(1, n+1):
        soma = soma + x**(-1)
    return round(soma, 2)