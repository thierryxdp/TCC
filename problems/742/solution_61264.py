def substitui(s,x,i):
    '''função que recebe uma string s, um caractere x e um número inteiro
    i entre 0 e o comprimento da string que retorna a string porém com o
    elemento na posição i substítuido pelo caeactere x
    str, int, int -> str'''
    if 0<=i<=len(s):
        return (s[0:i]+x+s[i+1:])