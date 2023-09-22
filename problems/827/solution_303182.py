def qtd_divisores(n):
    '''
    Conta o numeros de divisores de um dado numero.
    
    Entrada/Saida:
    int -> int
    '''
    div = 0
    for i in range(1, n + 1):
        if not (n % i):
            div += 1
	return div