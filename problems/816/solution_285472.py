def insere(lista_numero,n):
    '''Função que insere o número n na lista lista_numero de modo que ela fique ordenada de forma crescente
	lista, int -> lista'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''Função que dada uma lista e um número, retorna uma nova lista apenas com os números maiores que o número introduzido na lista
    lista, float -> lista'''
    copia=list.copy(lista)
    i=0
    while copia[i]<n:
    	del copia[i]    
        i=i+1
    return copia