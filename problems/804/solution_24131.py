#Start your python function here
def filtra_pares(n):
    f=()
    if n[0]%2==0:
        f=(n[0],)
    if n[1]%2==0:
        f=f+(n[1],)
    if n[2]%2==0:
        f=f+(n[2],)
    if n[3]%2==0:
        f=f+(n[3],)
    return f