def qtd_divisores(numero):
    """
    Essa função recebe um número e retorna quantos divisores 
    ele tem.
    int -> int
    """
    divisores = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    return len(divisores)