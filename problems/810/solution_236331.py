def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","")
    a = s.split()
    b= a[::-1]
    c = str.join(a,a[::-1])
    return b