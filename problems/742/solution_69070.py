'''Funcao que recebe uma string s, um caractere x
e um numero inteiro i entre 0 e o comprimento
da string e retorna a string igual a s, exceto
que o elemento da posicao i deve ser substituido por
x
string,char,int->string'''
def substitui(s,x,i):
    return s[0:i]+x+s[i+1:]