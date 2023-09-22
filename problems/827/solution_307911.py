def qtd_divisores(numero):
    qtd_div=0
    for i in range(numero):
        if numero % i == 0:
            qtd_div = qtd_div+1
	return qtd_div