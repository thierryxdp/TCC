def filtra_pares(entrada):
    """ Recebe um tupla de 4 elementos inteiros,
   caso sejam pares seram retornados na mesma ordem
   da entrada
   tupla -> tupla """
    if entrada[0]%2 == 0:
        primeiro = entrada[0]
    if entrada[1]%2 == 0:
        segundo = entrada[1]
    if entrada[2]%2 == 0:
        terceiro = entrada[2]
    if entrada[3]%2 == 0:
        quarto = entrada[3]
    return (primeiro,segundo,terceiro,quarto)