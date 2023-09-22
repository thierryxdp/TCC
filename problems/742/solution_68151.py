'''Esta função recebe do usuário uma string s, um caractere x e um número
inteiro i, em que i é um número inteiro entre 0 e o comprimento da string. O
retorno da função é uma string igual a essa, porém com o caractere x no lugar do
caractere da posição i da string.
str,str,int --> str'''
def substitui(s,x,i):
     var = s[:i]+x+s[i+1:]
    return var