# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string s, substituindo o elemento da posição de número i por um caractere x;
    str, int, int -> str'''
    s = str(s)
    x = s[i]
    return s+x