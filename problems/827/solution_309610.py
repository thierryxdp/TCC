def qtd_divisores(numero):
	div=0
    for i in range(numero):
        if numero<0:
           return 0
        if numero%i==0:
            div=div+1
    return div