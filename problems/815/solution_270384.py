def insere(lista_numero, n):
    '''dada uma lista ordenada na ordem crescente de números inteiros(lista_numero) e um número
    inteiro(n), retorna a lista com o número n incluso de forma que a lista continue ordenada;
    list, int -> list'''
	lista_numero.append(n)
    lista_numero.sort()
    return lista_numero