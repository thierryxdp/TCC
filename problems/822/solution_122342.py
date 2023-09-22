def repetidos(x):
    '''retorna a quantidade de vezes que em uma lista x um número é igual ao número anterior a ele
    list -> int'''
    
    cont = 0
    y = len(x)
    ocor = 0
    while cont < y:
        z = cont - 1 
        a = cont
        if x[a] == x[z]:
            ocor = ocor + 1
        cont = cont +1
	return ocor