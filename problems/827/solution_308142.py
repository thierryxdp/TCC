def qtd_divisores(numero):
    divisores = 0
    contador = 0
    while contador <= numero:
    	if numero%2 == 0:
       		divisores = divisores + 1
		contador = contador + 1
	return divisores