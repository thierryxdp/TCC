# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna, dados a string s, o caractere
    x e o número inteiro entre 0 e o comprimento da string, 
    uma string nova, igual a s, exceto que o elemento da 
    posição i deve ser substituído pelo caractere x
    str, float, int -> str'''
    len(s) *-1 <= i <= len(s) - 1
    return s[0:i] + str(x) + s[i+1:-1]