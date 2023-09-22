def filtraMultiplos(l,n):
    lista1= []
    a= 0
    b= len(l)
    while a<b:
        if (l[a]%n)==0:
            lista1= lista1 + [l[a]]
        a = a +1
	return lista1