def insere(lista_numero, n):
    '''Função que insere um dado número inteiro n qualquer em uma dada
    lista de números. Retornando a nova lista com o número n inserio na 
    ordem correta. list, int -> list'''
    list.insert(lista_numero, 0, n)
    list.sort(lista_numero)
    return lista_numero