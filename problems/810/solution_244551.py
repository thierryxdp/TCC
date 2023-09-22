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
    y = tiraponto(x)
    str.lower(y)
    str.split(y)
    list.reverse(y)
    z = ' '.join(y)
    return z