# Fuçao que recebe string, um caractere e um numero inteiro entre 0 e o
# comprimento da string e retorna uma string igual, porem o elemento da 
# posição é trocado pelo caractere  
# string, int, int -> string
def substitui(s,x,i):
    st[i] = x
    return st[0:1] + x + st[i+1:]