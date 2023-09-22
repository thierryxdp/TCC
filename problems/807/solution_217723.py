def conta_frases(a):
    
    b= len(str.split(a,'.')),
    c= len(str.split(list(b),'!')),
    d= len(str.split(list(c),'?')),
    e= len(str.split(list(e),'...'))
    return len(b+c+d+e)