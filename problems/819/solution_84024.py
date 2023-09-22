def filtraMultiplos(lista,num):
    lista_divisores=[]
    for elem in lista:
        if elem%num==0:
            lista_divisores.append(elem)
	return lista_divisores

def filtraMultiplosII(lista,num):
    lista_divisores=[elem for elem in lista if elem%num else pass]
	return lista_divisores

filtraMultiplos([20,22,11,7,19,26,1,3],3)