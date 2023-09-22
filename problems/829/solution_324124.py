def soma_h(N):
    """Dado o número n, calcula o valor de H e o retorna até quando N
    for inteiro e dado como entrada.
    assinatura:
    testes:
    """
    soma = 0
    N2 = 1
    contador = 0
    while contador != N:
        soma = soma + 1/N2
        N2 = N2 + 1
        contador = contador + 1
    return round(soma, 2)