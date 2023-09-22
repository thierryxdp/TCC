def uppCons(f):
    contador = 0
    f1 = ''
    while contador < len(f):
        if f[contador] not in 'AEIOUaeiouÃÕãõÁáÉéÍíÓóÚúÂâÊêÎîÔôÛûÀàÈèÌìÒòÙù':
            f1 = f1 + f[contador].upper()
        else:
            f1 = f1 + f[contador]
        contador = contador + 1
    return f1