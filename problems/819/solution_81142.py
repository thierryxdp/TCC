def filtraMultiplos(numero,n):
    list.sort(numero)
    i=0
    while numero[i] <= numero[len(numero)-1]:
        if numero[i]%n==0:
            lista1=list.append(numero[i])
		i=i+1
	return lista1