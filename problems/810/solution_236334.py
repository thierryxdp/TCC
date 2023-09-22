def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","").lower()
    a = s.split()
    b= a[::-1]
    c = a.join( ,b)
    return c