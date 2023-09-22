def inverte(f):
    f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    x=f.split()
    x=f.lower()
    x=f[::-1]
    return ''.join(x)