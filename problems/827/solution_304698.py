def qtd_divisores (n):
	''' funçao que conta quantos divisores um numero tem'''
	contagem = 0
	for i in range (1, n+1):
	     if n%i == 0:
		     contagem += 1
	return contagem