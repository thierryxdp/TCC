def conta_numero(numero, matriz):
    '''retorna a quantidade de vezes que um número é
    encontrado numa matriz
    int, list -> int'''
    count = []
    for lin in matriz:
        if numero in lin:
            count.append(numero)
 	return len(count)