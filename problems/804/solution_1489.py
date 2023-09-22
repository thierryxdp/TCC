def filtra_pares(tupla):
    """essa função recebe 4 numeros aleatórios e devolve apenas os pares"""
    r1 = tupla[0]%2
    r2 = tupla[1]%2
    r3 = tupla[2]%2
    r4 = tupla[3]%2
    if r1==0 and r2==0 and r3==0 and r4==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    elif r1==0 and r2==0 and r3==0 and r4!=0:
        return (tupla[0],tupla[1],tupla[2])
    elif r1==0 and r2!=0 and r3==0 and r4!=0:
        return (tupla[0],tupla[2])
    elif r1==0 and r2==0 and r3!=0 and r4!=0:
        return (tupla[0],tupla[1])
    elif r1!=0 and r2!=0 and r3!=0 and r4==0:
        return (tupla[3],)
    elif r1==0 and r2!=0 and r3==0 and r4==0:
        return (tupla[0],tupla[2],tupla[3])
    elif r1!=0 and r2!=0 and r3!=0 and r4!=0:
        return ()
    elif r1!=0 and r2!=0 and r3==0 and r4==0:
        return (tupla[2],tupla[3])
    elif r1!=0 and r2==0 and r3==0 and r4!=0:
        return (tupla[1],tupla[2])
    elif r1!=0 and r2==0 and r3==0 and r4==0:
        return (tupla[1],tupla[2],tupla[3])