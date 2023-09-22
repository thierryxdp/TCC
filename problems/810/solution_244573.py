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
    y = str.split(y)
    list.reverse(y)
    y = ' '.join(y)
    return y