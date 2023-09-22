#Start your python function here
def filtra_pares([tup]):
    if tup[0] % 2 == 0:
        n0 = tup[0]
        if tup[1] % 2 == 0:
            n1 = tup[1]
            if tup[2] % 2 == 0:
                n2 = tup[2]
                if tup[3] % 2 == 0:
                    n3 = tup[3]
                    return ('n0'+'n1'+'n2'+'n3')