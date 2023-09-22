def inverte(f):
    f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    x=f.split()
    x=f.lower()
    x=''.join(x)
    return x[::-1]