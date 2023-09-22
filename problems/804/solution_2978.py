def filtra_pares(tupla):
     '''função que dada uma tupla com quatro elementos inteiros retorna uma
    nova tupla com apenas os elementos pares da tupla original, na mesma ordem
    em que se encontravam; tuple (int, int, int, int) -> tuple'''
    nova_tupla = ()
    if tupla[0] % 2 == 0:
        nova_tupla = (tupla[0], )
    if tupla[1] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[1], )
    if tupla[2] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[2], )
    if tupla[3] % 2 == 0:
        nova_tupla = nova_tupla + (tupla[3], )
    return nova_tupla