# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dados uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, retorna uma string igual a s, exceto que o elemento da posição i é substituído pelo caractere x;
    str, str, int --> str'''
    return s[:i]+x+s[i+1:]