def uppCons(x):
    i=0
    a=''
    while i < len(x):
        if x[i] in 'bcdfghjklmnpqrtsvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            a = a + str.upper(x[i])
        else:
            a= a + x[i]
        i = i + 1
    return a