# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna uma str equivalente a str s na qual o elemento da posicao i, tal que
    i e um inteiro positivo, e substituido por uma caractere x
    str, str, int -> str'''
    s[i]='x'
    return str(s)