#Função que recebe uma string s, caractere x e número inteiro i e retorna uma string igual a s, exceto que o elemento da posição i deve ser substituido pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    str (s[i]=x)
    return s[0:i]+x+s[i+1:]