def insere(lista_numero,n):
    """
    	Função que dada uma lista ordenada (crescente) de 
        números inteiros e um número inteiro, inclua-o na 
        posição correta da lista.
    	list,int -> list
    """
    lista_numero.append(n)
    lista_numero = lista_numero.sort()
    return lista_numero