"""calcula e retorna uma string
string, string, int -> string"""
def substitui(s,x,i):
    if i==0:
        return x+s
    if 0<i<len(s):
        return (s[0:i])+x+(s[i:len(s))
    if i==len(s): 
        return s+x