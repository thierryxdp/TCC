def filtraMultiplos(lista,n):
    i=0
	resultado=[]
	while i<len(lista):
        if lista[i]%n==0:
        resultado.append(lista[i])
        i=i+1
    return resultado