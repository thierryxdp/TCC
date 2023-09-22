# Fuçao que recebe string, um caractere e um numero inteiro entre 0 e o
# comprimento da string e retorna uma string igual, porem o elemento da 
# posição é trocado pelo caractere  
# string, int, int -> string
def substitui(s,x,i):
    s[i] = x
    return str[:i] + x + str[i + 1:]