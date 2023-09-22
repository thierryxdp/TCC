#Start your python function here
def filtra_pares([a,b,c,d]):
    valores = (a,b,c,d)
    par = tuple(filter(lambda x: x%2 == 0, valores))
    return (par)