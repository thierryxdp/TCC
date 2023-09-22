#Start your python function here
def filtra_pares(t):
    if type(t) == tuple and len(t) == 4:
        for i in t and i%2 == 0:
                 lista.append(i)
        return(tuple(lista))