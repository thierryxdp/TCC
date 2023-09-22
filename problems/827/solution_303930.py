def qnd_divisores(x):
    '''funcao que conta quantos divisores um numero tem, int->int'''
	qtd=0
	for i in range(1,x+1):
		if x % i==0:
    		qtd+=1
    return qtd