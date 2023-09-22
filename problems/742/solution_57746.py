# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função retorna uma string "s" com seu caractere de número "i" substituido por um caractere "x"
    string, int, int -> string'''
    return s[:i] + x + s[(i+1):]