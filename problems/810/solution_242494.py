def inverte(f):
    f=f.replace(',',' ')
    f=f.replace('.',' ')
    f=f.replace('-',' ')
    f=f.replace(';',' ')
    f=f.replace(':',' ')
    f=f.lower()
    f=f.split(f)
    f=' '.join(f)
    f=f[::-1]
    return f