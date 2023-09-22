def inverte(txt):
    x= str.lower(txt.replace('...',' ').replace('-',' ').replace('.',' ').replace(',',' ').replace('?',' ').replace('!',' ').replace('.',' ').replace('/',' ').replace(':',' ').replace(';',' '))
    w = str.split(x)
    y = w[::-1]
    return str.join(' ',y)