def inverte(x):
    y = str.replace(y,'...',' ')
    y = str.replace(y,'.',' ')
    y = str.replace(y,'!',' ')
    y = str.replace(y,'?',' ')
    y = str.replace(y,'-',' ')
    y = str.replace(y,',',' ')
    y = str.replace(y,':',' ')
    y = str.replace(y,';',' ')
    y = str.lower(y)
    y = str.split(y)
    list.reverse(y)
    y = ' '.join(y)
    return y