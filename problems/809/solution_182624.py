def intercala(lista1, lista2):  
	lista=[]
    for i in lista1:
		lista.append(i)
		for e in lista2:
			if e not(in lista):
        		lista.append(e)
           
	return lista