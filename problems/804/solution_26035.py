#Start your python function here
def filtra_pares(t):
    lista = []
    if type(t) == tuple and len(t) == 4:
        if i%2 == 0:
            lista.append(i)
            return lista
        else:
            return ("Sem valores com 4 itens")