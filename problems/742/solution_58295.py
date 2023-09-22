# Função que dada uma string s, um caractere x e um inteiro i entre 0 e o comprimento de s, troca o elemento da posição i por x
# s: texto qualquer, x: caractere a ser inserido, i: posição na string, a: parte inicial de s, b: parte final de s
# str, str, int -> str
def substitui(s,x,i):
    a = s[:i]
    b = s[i+1:]
    return a + x + b