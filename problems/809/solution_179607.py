def intercala(lista1, lista2)
'''Função intercala duas listas, resultando em
uma terceira lista como união de ambas'''
'''list, list => list'''
    L1=lista1
    L2=lista2
    lista3=[L1[0]]+[L2[0]]+[L1[1]]+[L2[1]]+[L1[2]]+[L2[2]]
	return lista3