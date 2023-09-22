def qtd_divisores(n):
    """Recebe como parâmetro um número n e retorna o número de divisores de n;
    assinatura: float --> int
    Casos de teste:
    qtd_divisores(10) == 4
    qtd_divisores(100) == 9
    """
    z = 0
    for i in range(n + 1):
        if i != 0 and (n % i) == 0:
            z +=1
    return z