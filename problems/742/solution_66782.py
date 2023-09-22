''' função que dado uma string s na posição i entre 0 e o comprimento
da string, é substituido por um caracter x, retornando a string s
com o elemento substituido por x. 
str, int, int -> str'''
def substitui(s,x,i):
    return s[:i] + str(x) + s[::i]