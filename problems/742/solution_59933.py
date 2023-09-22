# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado uma string s, retorna substituindo na posição i o caractere x
    string, int, int -> string"""
    return s[:i]+x+s[i+1:]