def maiores(lista,n):
    lista_retorno=[]
    return [i for i in lista if i > n]
    lista_retorno= maiores(lista,n)
	list.sort(lista_retorno)
    print(lista_retorno)