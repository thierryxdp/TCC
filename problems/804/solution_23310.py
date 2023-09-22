#Start your python function here
def filtra_pares(a,b,c,d):
    l=[a,b,c,d]
    par = list(filter(lambda n:n%2==0,l))
    return par