#Start your python function here
def filtra_pares(tupla):
    "dada uma tupla na entrada cujos seus 4 elementos são inteiros, retorna uma tupla, apenas com os inteiros pares."
    novatupla = ()
    if tupla[0] % 2 == 0:
        novatupla = novatupla + (tupla[0],)
    if tupla[1] % 2 == 0:
        novatupla = novatupla + (tupla[1],)
    if tupla[2] % 2 == 0:
        novatupla = novatupla + (tupla[2],)
    if tupla[3] % 2 == 0:
        novatupla = novatupla + (tupla[3],)
    else:
        return ()