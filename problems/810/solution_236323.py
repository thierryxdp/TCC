def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","")
    a = str.split(s)
    b= a[::-1]
    c = str.join(a,b)
    return c