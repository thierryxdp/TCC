def qtd_divisores(numero):
    """Função que retorna a quantidade de divisores que o número dado como entrada tem
int -> int"""

    divisores = []

    for elemento in range(1, numero + 1):
        if numero % elemento == 0:
            divisores = divisores + [elemento]
    return len(divisores)