def qtd_divisores(n):
    '''calcula e retorna a quantidade de divisores que um numero tem.
    int -> int'''
    resultado = 0
    for c in range(1, n + 1):
        if n % c == 0:
            resultado += 1
    return resultado