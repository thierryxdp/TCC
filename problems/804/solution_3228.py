def filtra_pares(tupla):
    saida=()
    elemento1=int(tupla[0])
    elemento2=int(tupla[1])
    elemento3=int(tupla[2])
    elemento4=int(tupla[3])
    if elemento1%2==0:
        return saida+(elemento1,)
    elif elemento2%2==0:
        return saida+(elemento2,)
    elif elemento3%2==0:
        return saida+(elemento3,)
    elif elemento4%2==0:
        return saida+(elemento4,)
    if (elemento1%2==0 and elemento2%==0 and elemento3%2==0 and elemento4%2==0)==true:
        return saida+(elemento1,)+(elemento2,)+(elemento3,)+(elemento4,)
    else if (elemento1%2==0 and elemento2%==0 and elemento3%2==0):
        return saida+(elemento1,)+(elemento2,)+(elemento3,)
    else if (elemento1%2==0 and elemento2%==0):
        return saida+(elemento1,)+(elemento2,)
    else:
        return saida