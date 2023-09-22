def soma_h(N: int) -> float:
    """Essa função, dado um número inteiro N,
    calcula e retorna sua soma H com precisão de duas casas decimais"""
    soma = 0
    for i in list(range(1,N+1)):
        soma += 1/i
    return round(soma,2)