#Start your python function here
def filtra_pares(tupla):
    "dada uma tupla com 4 elementos inteiros, remove os elementos ímpares e retorna os pares novamente em uma tupla"
    novatupla = ()
    if tupla[0]%2==0:
        return novatupla + tupla[0]
    if tupla[1]%2==0:
        return novatupla + tupla[1]
    if tupla[2]%2==0:
        return novatupla + tupla[2]
    if tupla[3]%2==0:
        return novatupla + tupla[3]
    else:
        return ()