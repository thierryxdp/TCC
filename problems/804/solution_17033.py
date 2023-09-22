#Start your python function here
def filtra_pares (p):
    t=()
    if p[0]%2==0:
        t.append(p)
    if p[1]%2==0:
        t.append(p)
    if p[2]%2==0:
        t.append(p)
    if p[3]%2==0:
        t.append(p)
    return t