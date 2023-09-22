def insere(ls,n):
    '''Função que dada uma lista ordenada (crescente), de números inteiros,
    inclui um número n na posição correta, de forma que a lista 
    continue ordenada.
    assinatura: list, int -> list '''
	list.append(ls,n)
	list.sort(ls)
    return ls