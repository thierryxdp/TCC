# Função recebe uma string, um caratecre e um numero inteiro entre 0 e o 
# comprimento da string e retorna uma string igual mas substituindo a
#posição pelo caractere
# string, int, int -> string
def substitui(s,x,i):
    s = s[:i] + x + s[i+1]
    return s