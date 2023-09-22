def qtd_divisores(x):
    r = ()
    for a in list(range(x+1))[1::]:
        if x%a == 0:
            r += (a,)
    return r