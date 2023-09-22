def inverte(f):
    f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    x=f.split()
    x=f[::-1]
    x=''.join(f)
    return x