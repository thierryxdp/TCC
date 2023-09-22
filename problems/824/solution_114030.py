def uppCons(x):
    i = 0
    strFinal = ''
    while i < len(x):
        if not x[i] in 'aeiouAEIOUúóãéí':
            strFinal += str.upper(x[i])
        else:
            strFinal += x[i]
        i += 1
    return strFinal