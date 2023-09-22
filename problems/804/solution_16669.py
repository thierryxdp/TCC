def filtra_pares(t):
    ''' comentario. tuple->tuple.'''
    if t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return (t[0],t[1],t[2],t[3])
    if t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return (t[1],t[2],t[3])
    if t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        return (t[0],t[2],t[3])
    if t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        return (t[0],t[1],t[3])
    if t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return (t[0],t[1],t[2])
    if t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return ()

    if t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        return (t[2],t[3])
    if t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return (t[3])
    if t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        return (t[1],t[3])
    if t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return (t[0],t[3])
    if t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return (t[1],t[2])
    if t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        return (t[0],t[2])
    if t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        return (t[0],t[1])
    if t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return (t[0])
    if t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        return (t[1])
    if t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        return (t[2])