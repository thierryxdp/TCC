# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dados uam string s, um caractere x e um número inteiro
    i, a função retorna a string s com o elemento da posição i
    trocado pelo caractere x.
    string, string, int -> string'''
    return s[0:i]+x+s[i=1:]