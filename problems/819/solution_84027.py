def filtraMultiplosII(lista,num):
    lista_divisores=[elem for elem in lista if elem%num else pass]
	return lista_divisores
filtraMultiplosII([20,22,11,7,19,26,1,3],3)