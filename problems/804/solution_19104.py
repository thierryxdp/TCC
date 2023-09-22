#Start your python function here
def filtra_pares(s,i):
    if s[i]%2==0:
        return s[i]
    list(filter(filtra_pares,s))