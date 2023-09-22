# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dados uma string s, um caractere x e um número
    inteiro i entre 0 e o comprimento da string, retorna
    uma string igual a s, sendo substituído o elemento da
    posição i pelo caractere x.
    str, int, int -> str'''
    return s[0:i]+str(x)+s[(i+1):-1]+s[-1]