#  recebera uma string s, um caractere x e um nuero inteiro i entre 0 e o coprimento string, e retorne string isgual a s, exceto que o elemento da posiçao i deve ser substituido por x
# s,x,i
# string, int, int -> string
def substitui(s,x,i):
    s[i] = x
    # return s[0:i] + x + s[i + 1:]
    return s