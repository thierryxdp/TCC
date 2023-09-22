# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma string s, um caractere x e um numero inteiro i, com comprimento 
    da string entre 0 e string
    str, str, int -> '''
    assert type(s)is str and type(x) is str, 
    assert 0 < i < len (s), 
    return s[:i]+x[0]+s[i+s]