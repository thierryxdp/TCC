# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna uma string S, com o elemento da posição I substituído pelo caractere X.
    string, int, int -> string'''
    0<=i<=len(s)
    return s[0:i]+str(x)+s[i+1:]