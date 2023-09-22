#Start your python function here
def filtra_pares(a,b,c,d):
    tuple=[a,b,c,d]
    if a%2==0:
        return [a]
    elif b%2==0:
        tuple=[b]
        return [a,b]
    elif c%2==0:
        tuple[c]
        return [a,b,c]
    else:
        if d%2==0:
            tuple[d]
            return [a,b,c,d]
        else:
            return []