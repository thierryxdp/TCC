def uppCons(f):
    '''...'''
    i = 0
    f1 = ''
    while i < len(f):
        if (f[i]) not in 'aeiouàáãâèéêìíîòóôõùúû':
            f1 = f1 + f[i].upper()
        else:
            f1 = f1 + f[i].lower()
        i = i + 1
    return f1