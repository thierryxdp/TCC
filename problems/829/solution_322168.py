def soma_h(numero):
    h=0
    for n in range(1,numero+1):
        h += 1/n
    return round(h,2)