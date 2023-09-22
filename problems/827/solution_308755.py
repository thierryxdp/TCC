def qtd_divisores(n):
    ''' Função que retorna a quantidade de divisores um número tem.
    int --> int '''
    resultado = 0
    for d in range (1, n + 1):
        if n/d == n//d:
            resultado = resultado + 1
    return resultado