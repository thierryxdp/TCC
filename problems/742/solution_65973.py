# Função que recebe uma string, sendo uma caracter um inteiro e outro caracter, e retorna o caracter inteiro na posição do caracter x 
# string, int, int -> string
def substitui(s,x,i):
    s[i] = x
    return s1[0:i] + x + s1[i + 1:]