def maiores(lista_numeros,n):
    '''Função que retorna outra lista, que contenha todos os
números da lista de entrada maiores do que n, em ordem
crescente;
    lista,int -> lista'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    if n>lista_numeros[-1]:
        return []
    else:
    	del lista_numeros[0:list.index(lista_numeros,n,0,-1)]
    	return lista_numeros