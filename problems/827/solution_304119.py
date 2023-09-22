def qtd_divisores(numero):
    contador=0
	for indice in range(1,numero+1):
        if numero%indice==0:
        	contador=contador+1