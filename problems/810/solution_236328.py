def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","")
    a = s.split()
    b= a.reverse()
    
    return b