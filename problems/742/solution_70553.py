import re
def substitui(s,x,i): 
    letra=s[i]
    por=x
    a= s.replace(letra,por,0)
    return a