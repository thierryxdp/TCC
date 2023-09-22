def lingua_p(p):
    c = 0
    a = list(p)
    for i in a:
        if i in 'AEIOUaeiouÁáÉéÍíÓóÚúÃãÕõÂâÊêÎîÔôÛû':
            a[c] = i+'p'+i
        c = c + 1
    return str.join('',a)