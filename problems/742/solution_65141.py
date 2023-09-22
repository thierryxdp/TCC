# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorne uma
    string igual a s e o elemento da posição i deve ser substetuído pelo cactere x
    string, int, int -> string'''
    z=i+1
    return s[:i]+x+s[z:]