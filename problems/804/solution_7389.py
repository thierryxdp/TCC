def filtra_pares(a,b,c,d):
    '''
    Retorna os elementos pares da tupla
        Parametros:
            a,b,c,d: int
        Saida: tuple
    '''
    tupla = (a,b,c,d)
    if a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return tupla[0],
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return tupla[1],
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return tupla[2],
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        return tupla[3],
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return tupla[0],tupla[1]
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return tupla[0],tupla[2]
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return tupla[0],tupla[3]
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return tupla[1],tupla[2]
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return tupla[1],tupla[3]
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return tupla[2],tupla[3]
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return tupla[0],tupla[1],tupla[2]
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return tupla[0],tupla[1],tupla[3]
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return tupla[0],tupla[2],tupla[3]
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return tupla[1],tupla[2],tupla[3]
    elif a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return tupla[0],tupla[1],tupla[2],tupla[3]
    else:
        return tuple()#Start your python function here