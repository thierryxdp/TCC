def substitui(s,x,i):
    """# string, int, int -> string"""
    z = int(i)
    e = len(s)
    y = str(s)[:z] + x + str(s)[e:]
    return y