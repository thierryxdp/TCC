def inverte(f):
    f=f.replace('!',' ')
    f=f.replace('?',' ')
    f=f.replace('.',' ')
    f=f.replace(';',' ')
    f=f.replace(',',' ')
    f=f.replace('-',' ')
    f=f.reverse(f)
    return f