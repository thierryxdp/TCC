#Start your python function here
def filtra_pares(tupla):
    novatupla = ()
    if tupla[0]%2 == 0:
        novatupla = novatupla + (tupla[0],)
    if tupla[1]%2 == 0:
        novatupla = novatupla + (tupla[1],)
    if tupla[2]%2 == 0:
        novatupla = novatupla + (tupla[2],)   
    if tupla[3]%2 == 0:
        novatupla = novatupla + (tupla[3],)
    return novatupla