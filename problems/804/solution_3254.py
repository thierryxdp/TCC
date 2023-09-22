def tupla(t):
    t1 = tuple()
    
    if t[0]%2 == 0:
       t1 = t1 + tuple([t[0]])
    if t[1]%2 == 0:
       t1 = t1 + tuple([t[1]])
    if t[2]%2 == 0:
       t1 = t1 + tuple([t[2]])
    if t[3]%2 == 0:
       t1 = t1 + tuple([t[3]])
    return t1