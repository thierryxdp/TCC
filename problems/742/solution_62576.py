# Fuçao que recebe string, um caractere e um numero inteiro entre 0 e o
# comprimento da string e retorna uma string igual, porem o elemento da 
# posição é trocado pelo caractere  
# string, int, int -> string
def substitui(s,x,i):
    a[i] = x
    return a[0:1] + x + a[i+1:]