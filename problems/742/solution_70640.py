# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma string s, um caractere x e um numero inteiro i e faz a substituicao do caractere na posicao i por x.
    string, string, int->string'''
    return s[:i]+str(x)+s[i+1:]