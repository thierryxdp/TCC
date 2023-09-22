def filtraMultiplos(lista,n):
    lista1=[]
    numero=0
    while numero<len(lista):
        if lista[numero]%n==0:
            lista1=lista1+[lista[numero]]
            
		numero=numero+1
	return lista1