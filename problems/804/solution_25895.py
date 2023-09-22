#tupla -> tupla

def filtra_pares(t):
    if t[0]%2 == 0:
        final = ()+(t[0],)
    if t[1]%2 == 0:
        final = final+(t[1],)
    if t[2]%2 == 0:
        final = final+(t[2],)
    if t[3]%2 == 0:
        final = final+(t[3],)
    return final