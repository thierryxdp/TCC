# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que receba uma string s, um caractere x e um número inteiro i 
    entre 0 e o comprimento da string, e retorne uma string igual a
    s, exceto que o elemento da posição i deve ser substituído pelo 
    caractere x'''
    return s[0:i:1]+x+s[(i+1):[(i-1)::1]