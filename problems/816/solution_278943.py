def maiores(lista, n):
    lista2=[]
    lista3=[]
    k=0
    j=0
	for k in range (len(lista)): # procurar em todas as listas internas	
        	for j in range (k): # procurar em todos os elementos nessa lista
            	lista3.append(lista[k][j])
    i=0 
    while(i<len(lista)-1):
        if n<lista[i]:
            lista2.append(lista[i])
        i+=1
    return lista2