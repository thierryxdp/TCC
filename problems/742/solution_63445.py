# string, int, int -> string
def substitui(s,x,i):
    s[i]=x
    return str s[0:i]+x+s[1+:]