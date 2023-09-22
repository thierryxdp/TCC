def repetidos(lista):
    m=0
    for numero in range(1,len(lista)):
        if lista[numero]==lista[numero-1]:
        	m=m+1
    return range(lista)