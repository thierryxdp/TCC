def conta_numero(numero,matriz):
    '''int,list[list]->int'''
    vezes=0
for i in range(len(matriz)):
    for j in (matriz[i]):
        if j ==numero:
            vezes=vezes+1
	return vezes