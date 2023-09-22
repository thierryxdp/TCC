def insere(lista_numero,n):
    '''Funcao que dada uma lista ordenada (crescente) de numeros inteiros e um numero inteiro n, inclua na posicao correta, ou seja, de tal maneira que a lista continue ordenada.
    lista, int -> lista'''
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero

def acima_da_media(lista):
    n = sum(lista)
    if n in lista:
        list.sort(lista)
        acima = list.index(lista,n)
        return lista[acima+1:]
    else:
        return insere(lista)