def qtd_divisores(numero):
	'''Recebe um número inteiro e retorna quantos
    divisores esse numero tem
    
	int--> int'''
	
    contador = 0
	
    for elemento in range(1, numero):
	
    	if numero % elemento == 0:
			contador += 1
	
    if numero < 0:
    	return contador