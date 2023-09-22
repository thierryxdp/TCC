# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s dados a string (s), 
    um caractere x e um número inteiro (i) entre 0 e o
    comprimento da string"""
    s = str(s)
    x = str(x)
    i2 = i + 1
    if i >=0 and i<=len(s):
        return s[0:i] + x + s[i2:]