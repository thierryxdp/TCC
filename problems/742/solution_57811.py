# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string(s), um caractere(x) e um número inteiro(i) e retorna uma string s
    string, int, int->string'''
    return s[:i]+x+ s[i+1:]