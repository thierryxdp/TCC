#socorro
def check_even(x):
    if x%2==0:
        return True
    else:
        return False
def filtra_pares(n):
    lista=list(n)
    dado=filter(check_even, lista)
    return tuple(dado)