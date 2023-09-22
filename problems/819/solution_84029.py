def filtraMultiplosII(lista,num):
    lista_divisores=[elem if elem%num==0 else pass for elem in lista]
	return lista_divisores
filtraMultiplosII([20,22,11,7,19,26,1,3],3)