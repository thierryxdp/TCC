def qtd_divisores(numero):
    soma=0
    i=1
    while i<=numero:
    	if numero%i==0:
            soma=soma+i
    return soma