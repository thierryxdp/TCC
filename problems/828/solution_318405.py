def primo(numero):
    contador = 0
    for x in range(2, numero):
    	if numero % x == 0:
            contador = contador + 1
    return contador == 0