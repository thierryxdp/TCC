def insere(lista_numero,n):
    '''Dada uma lista ordenada com números inteiros e um n
    também inteiro, retorna a lista com n em sua posição 
    correta
    list,int -> list'''
    return list.sort(list.extend(lista_numero,[n]))