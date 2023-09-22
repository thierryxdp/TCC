# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que substitui um elemente de uma string por um caractere dado, numa posicao i;
    str, str, int -> str'''
    if 0 <= i <= len(s):
        return s[:i] + x + s[i+1:]