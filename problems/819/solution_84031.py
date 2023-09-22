def filtraMultiplos(lista,num):
        lista_div=[]
        for item in lista:
            if item%num==0:
                lista_div.append(elem)
	return lista_div

filtraMultiplos([20,22,21,6,3,2,4,9,5,33,30],3)