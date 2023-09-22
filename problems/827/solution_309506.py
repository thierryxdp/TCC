def qtd_divisores(num):
    """Função que recebe um inteiro e retorna o número de divisores inteiros possíveis. int -> int"""
    div = 0
    for x in range(1, num+1):
        if num % x == 0:
            div += 1
    return div