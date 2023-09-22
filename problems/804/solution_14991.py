def filtra_pares (tupla):
    if tupla[0]%2==0:
        t1=int(tupla[0])
    else:
        t1 = ()
    if tupla[1]%2==0:
        t2=int(tupla[1])
    else:
        t2=()
    if tupla[2]%2==0:
        t3=int(tupla[2])
    else:
        t3=()
    if tupla[3]%2==0:
        t4=int(tupla[3])
    else:
        t4=()
    return (t1,t2,t3,t4)