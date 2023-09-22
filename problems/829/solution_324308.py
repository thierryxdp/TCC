#dado um número inteiro retorna o somatório de 1/1 até 1/n aumentando o denominador em 1 até chegar em n
#int-->float
def soma_h(n):
	x=0
	for y in range(1,n+1):
		x+=1/y
	return x