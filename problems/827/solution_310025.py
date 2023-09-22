def qtd_divisores(numero):
    r = 0
    if numero >=1:
        for x in range(1, numero):
            if numero % x == 0:
                r = r+1
    if numero == 0:
        r = r+0
    if numero >=1:
        r = r+1
    return r