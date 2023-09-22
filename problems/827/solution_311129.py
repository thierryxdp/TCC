def qtd_divisores(numero):
    """Funcao recebe um numero e retorna a quantidade de divisores que o numero tem
    int -> int"""
    divisores = []
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(i)
    return len(divisores)