def filtra_pares(tupla):
    a = tupla[1]%2
    b = tupla[2]%2
    c = tupla[3]%2
    d = tupla[4]%2
    if a==0 and b==0 and c==0 and d == 0:
        return (tupla[1],tupla[2],tupla[3],tupla[4])
    elif a==0 and b==0 and c == 0:
        return (tupla[1],tupla[2],tupla[3])
    elif a==0 and b==0 and d == 0:
        return (tupla[1],tupla[2],tupla[4])
    elif a==0 and c==0 and d == 0:
        return (tupla[1],tupla[3],tupla[4])
    elif a==0 and b==0:
        return (tupla[1],tupla[2])
    elif a==0 and c==0:
        return (tupla[1],tupla[3])
    elif a==0 and d==0:
        return (tupla[1],tupla[4])
    elif a==0:
        return (tupla[1])
    elif b==0 and c==0 and d==0:
        return (tupla[2],tupla[3],tupla[4])
    elif b==0 and c==0:
        return (tupla[2],tupla[3])
    elif b==0 and d==0:
        return (tupla[2],tupla[4])
    elif b==0:
        return (tupla[2])
    elif c==0 and d==0:
        return (tupla[3],tupla[4])
    elif c==0:
        return (tupla[3])
    elif d==0:
        return (tupla[4])
    else:
        return ()