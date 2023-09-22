def qtd_divisores(numero):

	"""Recebe um numero inteiro e retona quantos divisores 
	esse nuemero possui; int->int."""
   
    divisores=[]
	for i in range(1, numero+1):
  		if numero % i == 0:
            divisores.append(numero)
    
    return len(divisores)