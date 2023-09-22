def inverte(s0):
    a = str.replace(s0,"."," ")
    b = str.replace(a,","," ")
    c = str.replace(b,"-"," ")
    d = str.replace(c,"!"," ")
    e = str.replace(d,"?"," ")
    f = str.replace(e,":"," ")
    g = str.replace(f,";"," ")
    s1 = str.split(g)
    return s1