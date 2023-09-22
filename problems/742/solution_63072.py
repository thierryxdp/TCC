#função substitui o lugar 'i' pelo caractere 'x'
#
def substitui(s,x,i):
    return s[0:i]+str(x)+ s[(1+i):]