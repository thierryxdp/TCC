def qtd_divisores(num):
    """Função que recebe um número e retorna a quantidade
    de seus divisores
    int -> int """
    d = 0
    for q in range(1, num + 1):
        if num%q == 0:
            d = d + 1
    return d