def substitui(s,x,i):
    """# string, int, int -> string"""
    z = int(i)
    e = len(s) + i
    y = str(s)[:z] + x + str(s)[z + 3:]
    return y