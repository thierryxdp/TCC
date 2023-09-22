def fatorial(numero):
    ''' Dado como entrada um numero, retorna o 
    fatorial desse numero
    int -> int'''
    contador = 1
    fatorial = 1
    while contador < (numero+1):
		fatorial = contador*(contador-1)
		contador +=1
	return fatorial