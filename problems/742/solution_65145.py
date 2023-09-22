"""calcula e retorna uma string"""
i=x
string, int, int -> string
def substitui(s,x,i):
    if i== 0:
        return x+(s(1:))
    if i==len(s):
        return(s(0:len(s)))+x
    if len(s)<i<len(s):
        (s(0::i)+x+(s(i+1:))