def inverte(s):
    s = s.replace("!","").replace("?","").replace("...","").replace(".","")
    a = s.split()
    b= s.reverse()
    
    return b