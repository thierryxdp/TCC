def filtramultiplcos(listadenumeros,n):
	lista=[]
    i=0
    while i<len(listadenumeros):
        if listadenumeros[i]%n==0:
            lista=lista+[listadenumeros[i]]
            i=i+1
    return lista