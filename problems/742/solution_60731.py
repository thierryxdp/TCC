# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''retorna uma string igual a string s, com o elemento
    da posicao i substituido pelo caractere x; str, str, int -> str'''
    return str(s[0:i]+str(x)+str(s[(i+1):])