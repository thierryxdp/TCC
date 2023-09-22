def insere(lista_numero, n):
    '''Dado uma lista de numeros em ordem crescente e um numero n, retorna a lista com o n dentro, na posicao correta.
    list, int -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero