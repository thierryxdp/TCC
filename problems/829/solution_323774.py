def soma_h(n):
	""" Esta função calcula  a soma de H n vezes 
	int -> int """
	soma = 0
	for i in range (1,n+1):
		soma += 1/i
	return round (soma,2)