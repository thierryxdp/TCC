def inverte(f):
    f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    f=x.split()
    f=x[::-1]
    f=''.join(x)
    return f