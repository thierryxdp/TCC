#Start your python function here
def filtra_pares(tup):
    if tup[0]%2 == 0 and tup[1]%2 !=0 and tup[2]%2 != 0 and tup[3]%2 !=0:
        return tup[0]
    elif tup[1]%2 == 0 and tup[0]%2 !=0 and tup[2]%2 != 0 and tup[3]%2 !=0:
        return tup[1]
    elif tup[2]%2 == 0 and tup[0]%2 !=0 and tup[1]%2 != 0 and tup[3]%2 !=0:
        return tup[2]
    elif tup[3]%2 == 0 and tup[0]%2 !=0 and tup[1]%2 != 0 and tup[2]%2 !=0:
        print "("+ tup[3]+",)"