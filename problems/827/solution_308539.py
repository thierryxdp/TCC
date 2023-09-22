def qtd_divisores(numero):
    '''Retorna a quantidade de divisores de determinado (numero)
    int -> int'''
    
    qtd_divisores = 0
    for i in range(0, numero):
    	if numero%i == 0:
            qtd_divisores += 1
            
	return qtd_divisores