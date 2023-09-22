def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","")
    a = str.split(s)
    b = str.join(a,s[-1:])
    return b