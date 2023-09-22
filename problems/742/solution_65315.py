""""retorna string s substituindo pelo caractere x da posicao i da mesma""""
 #substitui
# string, int, int -> string
def substitui(s,x,i):
    if i==0:
        return x + s[1:]
    elif i== len(s):
        return s[0:len(s)] + x
    else:
        return s[0:i] + x + s[i+1:]