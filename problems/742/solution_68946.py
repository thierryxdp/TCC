"""
string, int, int -> string
"""
def substitui(s,x,i):
    subs_x = s[0:i-1]
    continu = s[i-1:len(s)]
    return str(subs_x)+x+str(continu)