# string que recebe s, um caractere x e um numero inteiro i entre 0 
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    s[i] = x
    return s[i] + x + s[i] + 1