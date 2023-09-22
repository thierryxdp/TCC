def filtra_pares(entrada):
    """ Recebe um tupla de 4 elementos inteiros,
   caso sejam pares seram retornados na mesma ordem
   da entrada
   tupla -> tupla """
    lista = []
    if entrada[0]%2 == 0:
        lista = lista + entrada[0:1]
    if entrada[1]%2 == 0:
        lista = lista + entrada[1:2]
    if entrada[2]%2 == 0:
        lista = lista + entrada[2:3]
    if entrada[3]%2 == 0:
        lista = lista + entrada[3:4]
        return tuple(lista)