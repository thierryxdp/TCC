def repetidos(lista):
    i=1
    j=0
    elementos=0
    while j<len(lista):
        if lista[i] == lista[j]:
            elementos=elementos+1            
            i=i+1
            j=j+1
	return elementos