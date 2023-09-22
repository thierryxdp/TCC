def qtd_divisores(n):
    """ Essa função conta quantos divisores um número tem.
    int->int."""
    soma = 0
    for i in range(1, n):
        if n % i == 0: 
            soma = soma +1
    return soma+1
	for i in not range(1,n):
        if n <0:
    	return 0