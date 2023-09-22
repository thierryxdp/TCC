# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Substitui a string s colocando o caractere x na posição i
    str, int, int -> str"""
    return s[0:i]+str(x)+s[(i+1):]