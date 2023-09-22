# string, int, int -> string
def substitui(s,x,i):
    s[:i]+x+s[i+1:]
    return s