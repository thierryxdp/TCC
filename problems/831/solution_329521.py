def lingua_p(palavra):
    n = len(palavra)
    m = 0
    while (n>m):
        if palavra[m] in 'AEIOUáéíóúaeiou':
            palavra = str.replace(palavra,palavra[m],palavra[m]+'p'+palavra[m])
            n = len(palavra)
            m = m+3
        else:
            m=m+1
    return palavra