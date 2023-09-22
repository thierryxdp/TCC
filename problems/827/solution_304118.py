def qtd_divisores(numero):
    contador=0
	for indice in range(numero):
        if numero%indice==0:
        	contador=contador+1