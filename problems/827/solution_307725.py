def qtd_divisores(numero):
    h=[]
    for x in list(range(1,numero+1)):
        if numero % x == 0:
            list.append(h,x)
    return len(h)