def maiores(lista_numero,n):
    '''função que dada uma lista de números inteiros e um numero inteiro (n), retorna os números da lista originais maiores que n, ordenados em ordem crescente'''
    if n not in lista_numero:
        list.append(lista_numero, n)
        list.sort(lista_numero)
        i=list.index(lista_numero, n)
        return lista_numero[i+1:] 
    else:
        list.sort(lista_numero)
        i=list.index(lista_numero, n)
        return lista_numero[i+1:]