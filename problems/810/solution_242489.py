def inverte(f):
    f.replace(',',' ')
    f.replace('.',' ')
    f.replace('-',' ')
    f.replace(';',' ')
    f.replace(':',' ')
    f=f.lower()
    f=f.split()
    f=''.join(f)
    return f[::-1]