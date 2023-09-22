# Função que dada uma string s, um caractere x e um inteiro i entre 0 e o comprimento de s, troca o elemento da posição i por x
# s: texto qualquer, x: caractere a ser inserido, i: posição na string
# string, int or str, int -> string
def substitui(s,x,i):
    s[i] = x
    textonovo = s
    return textonovo