# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma str, um carectere e um numero inteiro entre 0 e o comprimento da str
    e retorna uma str
    str,str,int -> str'''
    s1 = s[:i]
    s2 = s[i+1:]
    return s1 + x + s2