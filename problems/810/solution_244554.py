def tiraponto(x):
    x = str.replace(x,'...',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    x = str.replace(x,'-',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,';',' ')
    x = str.lower(x)
    return x

def inverte(x):
    tiraponto(x)
    x = str.split(x)
    list.reverse(x)
    z = ' '.join(x)
    return z