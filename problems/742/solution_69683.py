# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que substitui o caractere de posição i da string s pelo caractere x
    str, int, int -> str'''
    strnova=s[0:i]+x+s[i+1:]
    return strnova