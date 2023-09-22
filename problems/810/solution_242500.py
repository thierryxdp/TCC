def inverte(f):
    f=f.replace(',',' ')
    f=f.replace('.',' ')
    f=f.replace('-',' ')
    f=f.replace(';',' ')
    f=f.replace(':',' ')
    f=f.replace('!',' ')
    f=f.replace('?',' ')
    f=f.lower()
    f=f.split()
    f=f[::-1]
    f=' '.join(f)
    return f