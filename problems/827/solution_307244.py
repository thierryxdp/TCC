def qtd_divisores(n):
    '''retirna a quandiadade de divisores de um numero dado;
    int->int'''
    divisores=[]
    for numero in range(n+1):
        if n%numero==0:
            list.append(divisores,numero)
	return len(divisores)