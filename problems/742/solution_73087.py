# faz a substituicao de s,x,i 
# string, int, int -> string
def substitui(s,x,i):
    0 < i <= len (s)
    return  s[0:i] + x + s [i+1:]