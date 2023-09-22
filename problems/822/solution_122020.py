def repetidos(lsita):
    i=1
    j=0
    elementos=0
    while j<len(lista):
        if lista[i] == lista[j]:
            i=i+1
            j=j+1
            elementos=elementos=1
	return elementos