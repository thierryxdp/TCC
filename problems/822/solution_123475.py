def repetidos(lista):
    i=0
    numeros=[]
    contador=0
    while i < len(lista):
        if (lista[i] in numeros) == False:
        	if (lista[i] in lista[i+1:]):
            	contador +=1
            	numeros.append(lista[i])
    	i+=1
    return contador