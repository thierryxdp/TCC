def qtd_divisores (n):
    contador = 0
    indice = 1
    while indice <= n:
    	if n%indice == 0:
            contador = contador +1
        indice = indice +1
    return contador