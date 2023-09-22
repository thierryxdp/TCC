def inverte(f):
    s=str.split(f)
    list.reverse(s)
    d=str.join('.',s)
    b=str.replace(d,'.',' ')
    return b