def intercala(lista1, lista2):
    '''funcao que dadas duas listas iniciais(lista1,lista2), retorna ambas intercaladas em uma lista 3(listanova)
    list-->list'''
	listanova=[]
    for i in range(len(lista1)):
    	listanova=listanova+[lista1[i],lista2[i]]
    return listanova