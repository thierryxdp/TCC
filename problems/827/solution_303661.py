def qtd_divisores(numero):
    """Função que conta a quantidade de divisores que um número tem.
    Entrada: int.
    Saída: int."""
    
    divisores = 0
    for i in range(1,numero+1):
        if i%2 == 0:
            divisores = divisores + 1
    return divisores