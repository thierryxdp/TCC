def qtd_divisores(n):
    """Calcula e retorna a quantidade de divisores de um numero
    int->int"""
    r = []
    for i in range(n):
        if i != 0:
        	if n%i == 0:
            	r.append(i)
    return len(r)