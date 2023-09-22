def soma_h (N):
	'''Calcula a soma dos inversos dos antecessores de 
    um número N dado;
    int -> float'''
    soma = 0
    for i in range (1,N+1):
        soma = soma + (1.0/i)
    return round (soma,2)