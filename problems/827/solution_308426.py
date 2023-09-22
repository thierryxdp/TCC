def qtd_divisores(numero):
    divisores=[]
	for i in range(1, numero+1):
  		if numero % i == 0:
            divisores += numero
    
    return len(divisores)