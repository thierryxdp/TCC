# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i, e retorna uma string; str, int, int-> str'''
    if i < 0 or i >= len (s):
        return ' i invalido'
    return s[:i] + x + s[i+1:]