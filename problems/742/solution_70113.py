#substitui
# string, int, int -> string
def substitui(s,x,i):
    """"retorna string s substituindo pelo caractere x da posicao i
    da mesma
    """"
    if i==0:
        return x + s[1:]
    elif i== len(s):
        return s[0:len(s)] + x
    return s[0:i] + x + s[i+1:]