def filtra_pares(tup):
    n1 = int(tup[0])
    n2 = int(tup[1])
    n3 = int(tup[2])
    n4 = int(tup[3])

    if n1%2 == 0 and n2%2 == 0 and n3%2 == 0 and n4%2 == 0:
        return tuple(tup)
    
    elif n1%2 > 0 and n2%2 > 0 and n3%2 > 0 and n4%2 > 0:
        return tuple()
    
    elif n1%2 == 0 and n2%2 == 0 and n3%2 == 0:
        return tuple(tup[0:3])
    
    elif n1%2 == 0 and n3%2 == 0:
        return tuple(tup[0:4:2])
    
    elif n1%2 == 0 and n2%2 == 0:
        return tuple(tup[0:2])
    
    elif n4%2 == 0:
        return tuple(tup[3:4:2])
    
    elif n1%2 == 0 and n3%2 == 0 and n4%2 == 0:
        return tuple(tup[0]+tup[3:4])