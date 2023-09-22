def substitui(s,x,i):
    """# string, int, int -> string"""
    z = int(i) - 1
    e = len(s) - 1
    y = str(s)[:z] + x + str(s)[e:]
    return y