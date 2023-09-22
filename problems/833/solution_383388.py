def conta_numero(numero,matriz):
    """Esta função recebe um número inteiro e uma matriz e retorna a quantidade de vezes que este número aparece na matriz 
    int,list -> int"""
    lista = []
    if matriz == []:
    c = 0    
    else:
    	while c < len(matriz): 
        	for i in matriz[c]:
        		if i == numero:
            		lista.append(i)
            c += 1
    	return len(lista)