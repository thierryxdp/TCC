def inverte(f):
    f=f.replace(',',' ')
    f=f.replace('.',' ')
    f=f.replace('-',' ')
    f=f.replace(';',' ')
    f=f.replace(':',' ')
    x=f.lower()
    x=f.split()
    x=f[::-1]
    x=' '.join(x)
    return x