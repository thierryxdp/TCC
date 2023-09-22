def filtra_pares(valores):
    if valores[0]%2==0 and valores[1]%2==0 and  valores[2]%2==0 and  valores[3]%2==0:
        return valores[0],valores[1],valores[2],valores[3]
    elif valores[0]%2==0 and valores[1]%2==0 and  valores[2]%2==0:
        return valores[0],valores[1],valores[2]
    elif valores[0]%2==0 and valores[2]%2==0 and  valores[3]%2==0:
        return valores[0],valores[2],valores[3]
    elif valores[0]%2==0 and valores[1]%2==0:
        return valores[0],valores[1]
    elif valores[0]%2==0 and valores[2]%2==0:
        return valores[0],valores[2]
    elif valores[0]%2==0 and valores[3]%2==0:
        return valores[0],valores[3]
    elif valores[1]%2==0 and valores[3]%2==0:
        return valores[1],valores[3]
    elif valores[0]%2==0:
        return valores[0],
    elif valores[3]%2==0:
        return valores[3],
    else:
        return tuple()