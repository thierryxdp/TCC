#socorro
filtra_pares(n):
    lista=[r0,r1,r2,r3]
    if int(n[0])%2==0:
        r0=n[0]
    elif int(n[0])%2==1:
        lista.remove(r0)
    
    elif int(n[1])%2==0:
        r1=n[1]
    elif int(n[1])%2==1:
        lista.remove(r1)
    
    elif int(n[2])%2==0:
        r2=n[2]
    elif int(n[2])%2==1:
        lista.remove(r2)
    
    elif int(n[3])%2==0:
        r3=n[3]
    elif int(n[3])%2==1:
        lista.remove(r3)
    
    resultado=lista
    return tuple(resultado)