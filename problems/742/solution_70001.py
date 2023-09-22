# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''A função colocará o caracter (x) na posição (i) da string (s).
    string, string, int -> string'''
    Qs = len(s)
    parte1 = s[0:i]
    parte2 = s[i+1:Qs]
    return parte1 + x + parte2