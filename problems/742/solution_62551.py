# string, int, int -> string
def substitui(s,x,i):
    return str(s[0:5]) + str(x) + str(s[i-1:])