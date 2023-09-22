#Start your python function here
def filtra_pares(tp):
    tp_par = []
    for c in tp:
        if c % 2 == 0:
            tp_par.append(c)
    return tuple(tp_par)