def conta_numero(numero,matriz):
    '''Recebe um número(int) e uma matriz(list) e retorna a contagem do número na matriz.'''
    contador=0
    for linha in matriz:
        for elemento in matriz[linha]:
            if elemento == numero:
                contador=contador+1
	return contador