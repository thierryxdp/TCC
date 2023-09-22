def insere(lista_numero,n):
    '''função que recebe uma lista de números inteiros e um número inteiro n e retorna a lista de números ordenada de forma crescente.
    (list,int) -> list'''
    insere_n = list.append(lista_numero,n)
    ordena_lista = list.sort(lista_numero)
    return lista_numero