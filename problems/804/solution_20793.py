def filtra_pares(tup):
    pares=()
    if tup[0]/2==tup[0]//2:
        return tup[0]

    if tup[1]/2==tup[1]//2:
        return tup[1]
    if tup[2]/2==tup[2]//2:
        return tup[2]
    if tup[3]/2==tup[3]//2:
        return tup[3]
    if not (tup[0]/2==tup[0]//2 and tup[1]/2==tup[1]//2 and tup[2]/2==tup[2]//2 and tup[3]/2==tup[3]//2):
        return ()