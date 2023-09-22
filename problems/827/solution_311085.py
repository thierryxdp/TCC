def qtd_divisores(n):
    """Função que conta o número de divisores que um número n possui;
    int -> int"""
    quantidade = 0
    for divisor in range(1,1+n):
    	if n%divisor==0:
            quantidade += 1
        else:
            quantidade = quantidade
    return quantidade