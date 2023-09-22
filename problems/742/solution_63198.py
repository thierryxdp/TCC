# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe string s, caractere x
    e numero inteiro i entre 0 e comp. da string
    igual a s e troca i por x'''
    return s[0:i]+x+s[i+1:]