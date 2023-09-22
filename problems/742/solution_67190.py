#funçao que substitui um caractere x no lugar do termo i de uma string s
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i]+x+s[i+1:]