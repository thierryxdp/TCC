def filtra_pares(tupla):
    """Essa função filtra os elementos pares da tupla.
    Como entrada temos uma tupla com quatro elementos, e como saída 
    temos uma tupla com os elementos pares;
    tuple->tuple"""
    numero_1= tupla[0]%2
    numero_2=tupla[1]%2
    numero_3=tupla[2]%2
    numero_4=tupla[3]%2
    if numero_1==0 and numero_2==0 and numero_3==0 and numero_4==0:
        return (tupla[0],tupla[1],tupla[2],tupla[3])
    elif numero_1==0 and numero_2==0 and numero_3==0:
        return (tupla[0],tupla[1],tupla[2])
    elif numero_1==0 and numero_2==0 and numero_4==0:
        return (tupla[0],tupla[1],tupla[3])
    elif numero_1==0 and numero_3==0 and numero_4==0:
        return ( tupla[0], tupla[2], tupla[3])
    elif numero_2==0 and numero_3==0 and numero_4==0:
        return ( tupla[1],tupla[2], tupla[3])
    elif numero_1==0 and numero_2==0:
        return tupla[0],tupla[1]
    elif numero_1==0 and numero_3==0:
        return (tupla[0],tupla[2])
    elif numero_1==0 and numero_4==0:
        return ( tupla[0],tupla[3])
    elif numero_2==0 and numero_3==0:
        return ( tupla[1], tupla[2])
    elif numero_2==0 and numero_4==0:
        return ( tupla[1], tupla[3])
    elif numero_3==0 and numero_4==0:
        return ( tupla[2], tupla[3])
    elif numero_1==0:
        return ( tupla[0],)
    elif numero_2==0:
        return ( tupla[1],)
    elif numero_3==0:
        return (tupla[2],)
    elif numero_4==0:
        return (tupla[3],)
    else:
        return ()