def intercala(lista1, lista2):
    """Função que dada duas listas de tamanho 3 retorna uma lista que intercala lista 1 e lista 2
    	list,list->list"""
    soma1 = lista1 [0:1] + lista2 [0:1]
    soma2 = lista1 [1:2] + lista2 [1:2]
    soma3 = lista1 [2:] + lista2 [2:]
    return soma1 + soma2 + soma3