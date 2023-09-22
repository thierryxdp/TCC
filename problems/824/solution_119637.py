def uppCons(t):

    for i in range(len(t)):
        if t[i] in 'bcdfghjklmnpqrstvwxyzç':
            f = f[:i] + str.upper(f[i]) + f[i+1:]

        return f