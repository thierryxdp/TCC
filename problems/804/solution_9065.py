#Start your python function here
def filtra_pares(t1,t2,t3,t4):
    tupla = [t1, t2, t3, t4]
    par = []
    x = lambda m: m % 2 == 0
    par = list(filter(x, tupla))
    return par