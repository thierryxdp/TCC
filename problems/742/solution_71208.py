# Substitui o caractere na posição i da string s pelo
# caractere x definido na função
# string, int, int -> string
def substitui(s,x,i):
    if x==0:
    	return x + (s[1:])
    elif x==(-1):
        return (s[:-2]) + x
    else:
    	return (s[:(i)])+(x)+(s[(i):])