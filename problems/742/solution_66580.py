# Função que com as entradas s,x e i, retorne uma string igual a s, alterando apenas o elemento da posição i pela letra x 
# s é uma string qualquer;x é uma letra qualquer e i é um número inteiro entre 0 e o comprimento da string 
# string, string, int -> string
def substitui(s,x,i):
    return s[0:(i-1)]+x+s[i:]