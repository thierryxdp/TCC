def uppCons(f):

    for i in range(len(f)):
        if f[i] in 'bcdfghjklmnpqrstvwxyzç':
            f = f[:i] + str.upper(f[i]) + f[i+1:]

    return f