def qtd_divisores(numero):
    h=[]
    for x in list(range(numero)):
        if numero%x == 0:
            list.append(h,x)
    return len(h)