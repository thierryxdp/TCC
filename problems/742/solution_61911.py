# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna uma string igual a s, exceto que o elemento da posição i é substituído pelo caractere x,
    dados uma string(s), um caractere(x) e um número inteiro(i) entre 0 e o comprimento da string s; str, str, int -> str'''
    n = s[:i]+x+s[i+1:]
    return n