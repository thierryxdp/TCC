def insere(lista_numero,n):
    '''função que dadas uma lista ordenada crescente de números e um numero n, retorna 
       a lista com o número n incluso na posição correta. list, int -> list'''
    lista_total = list.append(lista_numero, n)
    lista_ordenada = list.sort(lista_total)
    return lista_ordenada