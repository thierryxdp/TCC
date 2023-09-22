def soma_h(N):
	'''Esta função calcula a soma de frações com
	N termos onde cada fração tem denominador igual
	a sua posição na soma
	int -> float'''
    soma = 0
    for i in range (1,n+1):
        soma = soma + (1/i)
        
    return round(soma,2)