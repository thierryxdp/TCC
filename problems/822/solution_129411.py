def repetidos(lista):
    m=0
    for numero in range(lista):
        if lista[numero]==lista[numero-1]:
        	m=m+1
    return m