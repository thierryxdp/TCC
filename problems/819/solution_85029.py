def filtramultiplos(listadenumeros,n):
    '''função que filtra os multiplocs de um numero n. int->int'''
    lista=[]
    i=0
    while i<len(listadenumeros):
        if listadenumeros[i]%n==0:
            lista=lista+[listadenumeros[i]]
 			i=i+1  
 	return lista