def filtra_pares(entrada):
    """ Recebe um tupla de 4 elementos inteiros,
   caso sejam pares seram retornados na mesma ordem
   da entrada
   tupla -> tupla """
    lista = [:]
    if entrada[0]%2 == 0:
        x = tupla+ entrada[0:1]
    if entrada[1]%2 == 0:
        x = x + entrada[1:2]
    if entrada[2]%2 == 0:
        x = x + entrada[2:3]
    if entrada[3]%2 == 0:
        x = x + entrada[3:4]
        return x