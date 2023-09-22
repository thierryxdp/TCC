def inverte(f):
    
    f=f.replace('!',' ')
    f=f.replace('?',' ')
    f=f.replace('.',' ')
    f=f.replace(';',' ')
    f=f.replace(',',' ')
    f=f.replace('-',' ')
    f.reverse(f)
    return f