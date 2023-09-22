def inverte(f):
    split()
    
    f=f.replace('!',' ')
    f=f.replace('?',' ')
    f=f.replace('.',' ')
    f=f.replace(';',' ')
    f=f.replace(',',' ')
    f=f.replace('-',' ')
    f.reverse()
    return f