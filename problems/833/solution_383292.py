def conta_numero(numero,matriz):
    ''' '''
    contador=0
    for i in range(0,len(matriz[0])):
        if i==numero:
            contador=contador+1
        	else:
            	contador=contador
    return contador