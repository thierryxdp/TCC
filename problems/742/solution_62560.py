# string, int, int -> string
def substitui(s,x,i):
    return str(s[0:i]) + str(x) + str(s[i+1:])