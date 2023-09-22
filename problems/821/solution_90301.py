def fatorial(n):
    '''Função que dado um número, calcula o fatorial deste número;
    int -> int'''
    if n == 0:
        return 1
    else:
        recursivo = fatorial(n-1)
        resultado = n * recursivo
        return resultado