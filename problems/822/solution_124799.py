def repetidos(lista):

    contador = 0
    
    for i in range(1,len(lista)):
    	if lista[i] == lista[i-1]:
            contador = contador+1

    return a