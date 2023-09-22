def qtd_divisores(numero):
	div=0
    for i in range(numero,numero,1):
        if numero%i==0:
            div=div+1
    return div