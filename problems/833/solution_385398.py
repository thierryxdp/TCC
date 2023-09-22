def conta_numero(numero, matriz):
    "Retorne, dado um número inteiro quantas vezes aquele número aparece na matriz; int,list(list)->int"
	c=0
    for i in len(matriz):
        for ii in i:
            if ii==numero:
            	c+=1
    return c