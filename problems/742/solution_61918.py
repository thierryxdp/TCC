# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que retorna uma string com um caractere 'x' na posição de i.
    str,str,int->str'''
    return s[:i]+x+s[i+1:]