def filtraMultiplos(numero,n):
    list.sort(numero)
    i=0
    lista1=[]
    while numero[i] < numero[len(numero)]:
        if numero[i]%n==0:
            list.append(lista1,numero[i])
		i=i+1
	return lista1