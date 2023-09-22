def repetidos(lista):
    m=0
    for numero in range(1,lista):
        if lista[numero]==lista[numero-1]:
        	m=m+1
    return m