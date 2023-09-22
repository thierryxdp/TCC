def inverte(string):
    x=str.lower(string)
    x=str.replace(x,'.','')
    x=str.replace(x,',','')
    x=str.replace(x,'!','')
    x=str.replace(x,'?','')
    x=str.replace(x,'-',' ')
    x=str.split(x)
    list.reverse(x)
    str.join(,x)
    return x