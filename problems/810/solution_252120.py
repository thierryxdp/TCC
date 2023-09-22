def inverte(f):
    f2 = f.split(",")
    f2 = ''.join(f2)
    f2 = f2.split(".")
    f2 = ''.join(f2)
    f2 = f2.split("!")
    f2 = ''.join(f2)
    f2 = f2.split("?")
    f2 = ''.join(f2)
    
    return f2[::-1].lower()