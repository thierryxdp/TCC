def divisores(n):
    """Função que recebe um inteiro e retorna o número de divisores inteiros possíveis. int -> int"""
    divis = 0
    for x in range(1, n+1):
        if n % x == 0:
            divis += 1
    return divis