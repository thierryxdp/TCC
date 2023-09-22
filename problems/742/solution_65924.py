""" Dados uma string "s", um carctere "x"
e um número inteiro "i" entre 0 e o comprimento
da string, retorna uma string "s" com o caractere
da posição "i" sendo substituído por "x" 
string, int, int -> string"""
def substitui(s,x,i):
    p = s[i]
    return s.replace(p,x)