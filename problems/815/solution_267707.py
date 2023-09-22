def insere(lista_numero,n):
    '''Função que dado uma lista de numeros inteiros e um numero inteiro n 
    retorna uma lista ordenada do menor numero para o maior incluindo o inteiro n
     list, int -> list'''
    lista = lista_numero +[n]
    list.sort(lista)
    return lista