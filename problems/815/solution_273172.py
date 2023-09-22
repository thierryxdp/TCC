def insere(lista_numero,n):
    """Função que recebe uma lista e um numero inteiro e inclue o numero n na sua posição correta na ordem crescente."""
    """list, int->list"""
    lista_numero=lista_numero+[n]
    return list.sort(lista_numero)