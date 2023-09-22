def soma_h(N):
    """Retorna o valor H de acordo com a equação dada no exercício.
    Entrada: int
    Saída: float
    """
    contagem = 0
    soma = 0
    while contador < N:
        soma += 1/(contador+1)
        contador += 1
    return round(soma, 2)