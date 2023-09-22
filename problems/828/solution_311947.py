def primo(n):
    '''Dado um número, a função retorna se ele é primo ou não
       int -> bool
       Parametros:
       n: numero a ser digitado'''
    i = 0
    for c in range(1, n + 1):
        if n % c:
            i += 1
    if i > 2:
        return False
    else:
        return True