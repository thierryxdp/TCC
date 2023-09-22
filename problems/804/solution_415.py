#Start your python function here
def filtra_pares(tupla):
    """Retorna uma nova tupla com apenas os elementos pares da tupla de quatro inteiros recebida na mesma ordem;
    tuple(int, int, int, int) -> tuple"""
    n1 = tupla[0]%2 == 0
    n2 = tupla[1]%2 == 0
    n3 = tupla[2]%2 == 0
    n4 = tupla[3]%2 == 0
    if n1 and n2 and n3 and n4:
        return (tupla[0], tupla[1], tupla[2], tupla[3])
    elif n1:
        if n2 and n3:
            return (tupla[0], tupla[1], tupla[2])
        elif n2 and n4:
            return (tupla[0], tupla[1], tupla[3])
        elif n3 and n4:
            return (tupla[0], tupla[2], tupla[3])
        elif n2:
            return (tupla[0], tupla[1])
        elif n3:
            return (tupla[0], tupla[2])
        elif n4:
            return (tupla[0], tupla[3])
        else:
            return (tupla[0],)
    elif n2:
        if n3 and n4:
            return (tupla[1], tupla[2], tupla[3])
        elif n3:
            return (tupla[1], tupla[2])
        elif n4:
            return (tupla[1], tupla[3])
        else:
            return (tupla[1],)
    elif n3:
        if n4:
            return (tupla[2], tupla[3])
        else:
            return (tupla[2],)
    elif n4:
        return (tupla[3],)
    else:
        return ()