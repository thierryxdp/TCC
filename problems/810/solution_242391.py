def inverte(f):
    f=f.split()
    f=f[-1::]
    f=f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    return f