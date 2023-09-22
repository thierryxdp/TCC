def uppCons(f):
    ''
    newf = ''
    for lcons in f:
        if lcons in 'ZXCVBNMSDFGHJKLQWRTYPzxcvbnmsdfghjklqwrtyp':
            newf += lcons.upper()
        else:
            newf += lcons
    return newf