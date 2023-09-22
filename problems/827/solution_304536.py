def qtd_divisores(num):
    sequencia = list(range(1,num+1))
    contador = 0
                     
    for i in sequencia:
		if num % i == 0:
            contador += 1
	return contador