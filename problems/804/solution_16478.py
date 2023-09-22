def filtra_pares(numero):
    pares=(numero)
    if numero[0]%2==0 and numero[1]%2==0 and numero[2]%2==0 and numero[3]%2==0:
        pares=(numero[0],numero[1],numero[2],numero[3])
    elif numero[0]%2!=0 and numero[1]%2!=0 and numero[2]%2!=0 and numero[3]%2!=0:
        pares=()
    elif numero[0]%2==0 and numero[1]%2!=0 and numero[2]%2!=0 and numero[3]%2!=0:
        pares=(numero[0],)
    elif numero[0]%2==0 and numero[1]%2!=0 and numero[2]%2!=0 and numero[3]%2==0:
        pares=(numero[0],numero[3])
    elif numero[0]%2!=0 and numero[1]%2!=0 and numero[2]%2==0 and numero[3]%2!=0:
        pares=(numero[2],)
    elif numero[0]%2==0 and numero[1]%2!=0 and numero[2]%2==0 and numero[3]%2==0:
        pares=(numero[0],numero[2],numero[3])
    elif numero[0]%2!=0 and numero[1]%2!=0 and numero[2]%2!=0 and numero[3]%2==0:
        pares=(numero[3])
    return (pares)