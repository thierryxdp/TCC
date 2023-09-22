# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe string, caractere, numero e comprimento da string
    retorna uma string s'''
    'str,str,int->str'
    return s[:i] + x + s[i+1:]