def insere(lista_numero, n):
    '''Função que retorna o uma lista de números em ordem crescente das infomações ("lista" = lista de números, "n" = número aleatório a ser inserido na lista) de entrada: list, int -> list'''
    
    lista = lista_numero + [n,]
    list.sort(lista)
    
    return lista