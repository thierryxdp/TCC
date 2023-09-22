def qtd_divisores(numero):
    if numero <= 0:
        return 0 
    else:
        cont = 0
        for i in range(1,abs(numero) + 1):
            if numero%i == 0:
                cont+=1
	return cont