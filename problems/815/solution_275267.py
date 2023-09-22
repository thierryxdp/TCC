def insere1(lista_numero,n):
    """retorna uma lista com todos os elementos na 
    posicao em ordem crescente de modo que n seja
    acrescentado e mesmo assim a lista continue na
    ordem crescente.
    list, int -> list"""
    nova_lista = lista_numero[:]
    nova_lista.append(n)
    nova_lista.sort()
    return nova_lista