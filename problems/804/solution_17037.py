#Start your python function here
def filtra_pares (p):
    t=()
    if p[0]%2==0:
        t=t + (p[0],)
    if p[1]%2==0:
        t=t + (p[1],)
    if p[2]%2==0:
        t=t + (p[2],)
    if p[3]%2==0:
        t=t + (p[3],)
    return t