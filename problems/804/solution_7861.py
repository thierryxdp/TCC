#Start your python function here
def filtra_pares(tup):
    if int(tup[0])%2==0 and int(tup[1])%2==0  and int(tup[2])%2==0  and int(tup[3])%2==0:
        return tuple(tup)
    elif int(tup[0])%2==0 and int(tup[1])%2==0  and int(tup[2])%2==0:
        return tuple(tup[0:3])
    elif int(tup[0])%2==0 and int(tup[1])%2==0  and int(tup[3])%2==0:
        return tuple(tup[0:2], tup[3])