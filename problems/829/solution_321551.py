def soma_h(n):
    """Função que dado um número n, calcula e retorna
o valor H com n termos; int -> float """
    soma = 0
    for c in range(1, n + 1):
        inv = (1/c)
        soma += inv
    return round(soma, 2)