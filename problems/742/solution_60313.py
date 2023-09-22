# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado a função S,X,I, da uma string = S, porém na posição i mudando o X. """
    return s[0:i]+x+s[i+1:]