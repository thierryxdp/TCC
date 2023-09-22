def conta_numero(numero,matriz):
    '''Conta quantas vezes um numero aparece em uma dada matriz.
    int, list -> int'''
	x=numero
	y=matriz
    a=0
    for i in range(len(y)):
        if x==y[i]:
            a+=1
    return a