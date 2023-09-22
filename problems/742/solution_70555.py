import re
def substitui(s,x,i): 
    letra=s[i::]
    por=x
    a= s.replace(letra,por,1)
    return a