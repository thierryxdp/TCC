def inverte(f):
    f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    f.lower()
    x=f.split()
    x=f[::-1]
    return ''.join(x)