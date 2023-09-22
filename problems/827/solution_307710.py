def qtd_divisores(numero):
    h=[]
    for x in numero:
        if x%numero==0:
            h=h+x
        else:
            continue
    return h