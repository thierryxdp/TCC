# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que retorne uma string com o x no lugar do i"""
    return s[0:i-1]+x+s[i:]