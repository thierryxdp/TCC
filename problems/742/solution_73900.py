'''Função retorna um caractere x e um numero inteiro'''
# string, int, int -> string
def substitui(s,x,i):
    l = list(s)
    l[i]= x
    return (s[0:i]+x+s[i+1])