# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dada a string s, substitui o elemento na posição i por x"""
    return s[:i-1]+x+s[i:]