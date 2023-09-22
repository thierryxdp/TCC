#Start your python function here
def filtra_pares(a):
    l=[a]
    par = list(filter(lambda n:n%2==0,l))
    return par