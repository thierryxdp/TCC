'''Insere um numero dentro de uma lista na posição certa.
list, int --> list'''

def insere(lista_numero, n):
    list.insert(lista_numero, 1, n)
    list.sort(lista_numero)
   
    return lista_numero