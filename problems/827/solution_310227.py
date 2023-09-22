def qtd_divisores(n):
    """Dado n como um inteiro, retorna a quantidade de divisores dele 
    assinatura:
    int -> int
    testes:
    qtd_divisores(2) == 2
    qtd_divisores(7) == 2
    """
    ls = []
    for e in range(1, n+1):
        if n % e == 0:
            ls.append(e)
    return len(ls)