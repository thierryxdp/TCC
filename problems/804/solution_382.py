#Start your python function here
def filtra_pares(tupla):
    tuple_values = list()
    (a, b, c, d) = tupla
    if (a % 2) == 0:
        tuple_values.append(a)
    if (b % 2) == 0:
        tuple_values.append(b)
    if (c % 2) == 0:
        tuple_values.append(c)
    if (d % 2) == 0:
        tuple_values.append(d)
    return tuple(tuple_values)