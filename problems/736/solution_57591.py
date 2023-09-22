def concatencao(a,b):
    return str(a)+str(b)+str(b)+str(a)
def substitui(s,x,i):
    if i<0 or i>len(s):
        return "erro"
    else:
        s[i] =(x)