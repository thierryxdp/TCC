def uppCons(f):
    ''
    newf = ''
    for lcons in f:
        if lcons in 'ZXCVBNMSDFGHJKLQWRTYPzxcvbnmsdfghjklqwçrtyp':
            newf += lcons.upper()
        else:
            newf += lcons
    return newf