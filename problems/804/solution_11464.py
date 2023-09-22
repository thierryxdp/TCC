#Start your python function here
def filtra_pares(tuple):
    final = ()
    if tuple[0] % 2 == 0:
        final += (tuple[0],)
    if tuple[1] % 2 == 0:
        final += (tuple[1],)
    if tuple[2] % 2 == 0:
        final += (tuple[2],)
    if tuple[3] % 2 == 0:
        final += (tuple[3],)
    return final