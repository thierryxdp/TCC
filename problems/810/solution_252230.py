def inverte(f):
    f2= f.split(",")
    f2= ''.join(f2)
    f2= f2.split(".")
    f2= ''.join(f2)
    f2= f2.split("!")
    f2= ''.join(f2)
    f2= f2.split("?")
    f2=''.join(f2)
    f2= f2.split("-")
    f2= ''.join(f2) 
    f2= f2.lower()
    f3= f2.split()[::-1]
    return''.join(f3)