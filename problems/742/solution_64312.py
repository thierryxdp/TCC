# Função que recebe uma string s um caractere x e um númeo inteiro i entre 0 e o comprimento da string e retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x
# i é inteiro entre 0 e comprimento da string, s é uma string e x um caractere
# string, string, int -> string
def substitui(s,x,i):
    if i==0:
        return x+ s[1:]
    else:
        return s[0:i] + x + s[i+1:]