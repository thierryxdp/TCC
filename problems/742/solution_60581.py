# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ função que recebe uma string s, um caractere x  e um numero inteiro i 
    entre 0 e o comprimento da string e retorna uma string igual a s. Exceto que o 
    elemento que esta na posição i tenha que se substituido pelo caractere x
    str, str , int --> str"""
    sub_s1 = s[i]
    return s.replace(sub_s1, x , -1)