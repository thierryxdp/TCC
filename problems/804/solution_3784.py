def filtra_pares(a,b,c,d):
    """Funcao que dado 4 numeros, retorna apenas os pares na mesma ordem de entrada"""
    lista1=[a,b,c,d]
    lista2=[]
    for valor in lista1:
	    if valor % 2 == 0:
		    lista2.append(valor)

    print(lista2)