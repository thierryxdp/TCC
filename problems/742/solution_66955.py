# string que recebe s, um caractere x e um numero inteiro i entre 0 
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(string1,x,i):
    string1[i] = x
    return string1[i] + x + string1[i] + 1