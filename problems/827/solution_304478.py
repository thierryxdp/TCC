def qtd_divisores(n):
    '''Calcula a quantidades de divisores que (n) o parametro passado tem;
    	int --> int'''
    soma = 0
    for c in range(1, n+1):
        if n % c == 0:
            soma += 1
    return soma