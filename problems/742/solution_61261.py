# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(str:s,str:x,i):
    '''função que recebe uma string s, um caractere x e um número inteiro
    i entre 0 e o comprimento da string que retorna a string porém com o
    elemento na posição i substítuido pelo caeactere x
    str, int, int -> str'''
    if 0<=i<=len(s):
        return (s[0:i]+x+s[i:])