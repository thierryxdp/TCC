def qt_divisores(numero):
    '''Função que retorna a quantidade de divisores do número 
    fornecido como parametro 
    int -> int'''
    divisores = 0
    for indice in range(1, numero + 1):
        if numero % indice == 0:
            divisores += 1
	return divisores