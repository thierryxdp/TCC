def conta_numero(numero,matriz):
    '''Recebe um número(int) e uma matriz(list) e retorna a contagem do número na matriz.'''
    contador=0
    while linha < len(matriz):
        for elemento in matriz[linha]:
            if elemento == numero:
                contador+=1
        linha+=1
	return contador