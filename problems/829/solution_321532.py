def soma_h(N: int)-> float:
    """Dado um número inteiro (N), a função calcula e retorna o valor de H
    sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N"""
    H = list()
    for numero in range(1, N+1):
        list.append(H, 1/numero)
    return sum(H)