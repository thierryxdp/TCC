def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","").lower()
    a = s.split()
    b= a[::-1]
    c = b.join(" ",a)
    return c